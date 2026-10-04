"""Atualiza _data/metrics.json e _data/publications_sync.json.

A lista de artigos vem do ORCID (fonte oficial, mantida pelo autor); o
OpenAlex fornece ano/periódico/acesso aberto de cada DOI. Citações, h-index e
i10-index vêm do perfil público do Google Scholar (robots.txt permite
/citations?user=); se o Scholar falhar, mantém os últimos valores obtidos.

Usado pela página inicial (_pages/about.md): "Academic metrics" e
"Recent publications". Só regrava os arquivos quando os dados mudam.
Sem dependências externas (apenas biblioteca padrão).
"""
import datetime
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ORCID = "0000-0002-6129-1820"
SCHOLAR = "https://scholar.google.com/citations?user=KorU-HsAAAAJ&hl=en"
OPENALEX = "https://api.openalex.org"
DATA = Path(__file__).resolve().parent.parent / "_data"

# símbolos LaTeX comuns em títulos -> Unicode
LATEX = {r"\lambda": "λ", r"\alpha": "α", r"\beta": "β", r"\gamma": "γ",
         r"\Delta": "Δ", r"\delta": "δ", r"\Lambda": "Λ", r"\phi": "φ",
         r"\mathbb{T}": "T", r"\mathcal{T}": "T"}
# nomes de periódico que vêm malformados do OpenAlex
PERIODICOS = {"Physical review. D": "Physical Review D"}


def get(url):
    for tentativa in range(4):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "lcnsantos.github.io metrics", "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception:
            if tentativa == 3:
                raise
            time.sleep(5 * (tentativa + 1))


def scholar():
    """{'citations', 'h_index', 'i10_index'} (totais) do perfil, ou None se falhar."""
    try:
        req = urllib.request.Request(SCHOLAR, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/130.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"})
        with urllib.request.urlopen(req, timeout=60) as r:
            pagina = r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"Google Scholar indisponível: {e}")
        return None
    linhas = dict((rotulo, int(total)) for rotulo, total in re.findall(
        r'class="gsc_rsb_sc1"><a[^>]*>([^<]+)</a></td><td class="gsc_rsb_std">(\d+)</td>', pagina))
    if not {"Citations", "h-index", "i10-index"} <= linhas.keys():
        print("Google Scholar: tabela de métricas não encontrada (captcha?)")
        return None
    return {"citations": linhas["Citations"], "h_index": linhas["h-index"],
            "i10_index": linhas["i10-index"]}


def limpa_titulo(t):
    t = re.sub(r"<[^>]+>", "", t or "")
    for k, v in LATEX.items():
        t = t.replace(k, v)
    t = t.replace("$", "").replace("\\", "")
    return re.sub(r"\s+", " ", t).strip()


def limpa_periodico(nome):
    nome = (nome or "").split("/")[0].strip().rstrip(".")
    return PERIODICOS.get(nome, nome)


def norm_doi(doi):
    return re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", (doi or "").strip().lower())


def obras_orcid():
    """{doi: resumo ORCID} de cada obra com DOI."""
    d = get(f"https://pub.orcid.org/v3.0/{ORCID}/works")
    obras = {}
    for g in d.get("group", []):
        s = g["work-summary"][0]
        ids = (s.get("external-ids") or {}).get("external-id", [])
        doi = next((norm_doi(i["external-id-value"]) for i in ids
                    if i["external-id-type"] == "doi"), None)
        if doi and "arxiv" not in doi:
            obras.setdefault(doi, s)
    return obras


def obras_openalex(dois):
    """{doi: obra OpenAlex}, consultando em lotes."""
    achadas, dois = {}, list(dois)
    for i in range(0, len(dois), 40):
        filtro = "doi:" + "|".join(dois[i:i + 40])
        d = get(f"{OPENALEX}/works?per-page=50&filter={urllib.parse.quote(filtro, safe=':|')}")
        for w in d["results"]:
            achadas[norm_doi(w.get("doi"))] = w
    return achadas


def artigos():
    orcid = obras_orcid()
    oa = obras_openalex(orcid)
    saida = []
    for doi, s in orcid.items():
        w = oa.get(doi)
        if w:
            src = ((w.get("primary_location") or {}).get("source") or {})
            item = {
                "title": limpa_titulo(w.get("title")),
                "journal": limpa_periodico(src.get("display_name")),
                "year": w.get("publication_year"),
                "publication_date": w.get("publication_date"),
                "is_open_access": bool((w.get("open_access") or {}).get("is_oa")),
            }
        else:  # ainda não indexado no OpenAlex: usa só o ORCID
            ano = ((s.get("publication-date") or {}).get("year") or {}).get("value")
            item = {
                "title": limpa_titulo(s["title"]["title"]["value"]),
                "journal": limpa_periodico((s.get("journal-title") or {}).get("value")),
                "year": int(ano) if ano else None,
                "publication_date": f"{ano}-01-01" if ano else "",
                "is_open_access": False,
            }
        item["doi"] = f"https://doi.org/{doi}"
        saida.append(item)
    return sorted(saida, key=lambda x: x["publication_date"] or "", reverse=True)


def grava_se_mudou(nome, dados):
    """Grava _data/<nome> só se o conteúdo (ignorando 'updated') mudou."""
    caminho = DATA / nome
    if caminho.exists():
        antigo = json.loads(caminho.read_text(encoding="utf-8"))
        antigo.pop("updated", None)
        if antigo == dados:
            print(f"{nome}: sem mudanças")
            return
    dados = {"updated": datetime.date.today().isoformat(), **dados}
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{nome}: atualizado")


def main():
    pubs = artigos()
    grava_se_mudou("publications_sync.json", {"source": "ORCID + OpenAlex", "works": pubs})

    s = scholar()
    if s is None:  # mantém os últimos valores do Scholar já gravados
        print("metrics.json: mantido (Scholar indisponível)")
        return
    grava_se_mudou("metrics.json", {
        "source": "Google Scholar",
        "summary": {
            "works_count": len(pubs),
            "cited_by_count": s["citations"],
            "h_index": s["h_index"],
            "i10_index": s["i10_index"],
        },
    })


if __name__ == "__main__":
    main()
