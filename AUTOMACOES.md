# Automações do site

Arquivo de referência (não é publicado no site; está em `exclude` no `_config.yml`).

## 1. Robô externo: publicações (ORCID) e preprints gr-qc (arXiv)

- **O que faz:** reescreve `_pages/publications.md` (lista do ORCID) e `_pages/preprints.md`
  (feed gr-qc do arXiv, com gráficos embutidos em base64).
- **Frequência:** 1 vez por dia, em horário variável (entre ~12h e ~16h de Brasília).
  Gera 2 commits por execução ("Atualizando o conteúdo da página de publicações"),
  o primeiro em `publications.md` e o segundo em `preprints.md`, ~3 s de intervalo.
- **Onde roda:** **fora do GitHub Actions** e **fora deste PC** (verificado em 04/10/2026:
  nenhum workflow no repositório, nenhuma tarefa agendada no Windows, nenhum script
  encontrado nas pastas de usuário). Os commits saem sem assinatura e com o próprio
  usuário como committer, o padrão de um script que usa a API do GitHub
  (ex.: PyGithub `update_file`) com um **token pessoal (PAT)** da conta `lcnsantos`.
  Prováveis locais: outro computador, PythonAnywhere, Google Colab/Cloud ou VPS.
- **Token:** PAT da conta `lcnsantos` (escopo `repo` ou fine-grained com `contents: write`).
  Conferir/renovar em GitHub → Settings → Developer settings → Personal access tokens.
  Se o token expirar, o robô para silenciosamente.
- **Pendências:** localizar o script e anotar aqui o local; ele cria commits vazios
  quando nada muda (item 2b) e embute imagens no `.md` (item 2c).

## 2. Workflow `metrics.yml` (GitHub Actions): publicações recentes

- **O que faz:** roda `scripts/fetch_openalex.py`, que gera `_data/publications_sync.json`
  (bloco "Recent publications" da página inicial, 5 artigos mais recentes).
- **Fontes:** lista de artigos = **ORCID** (só obras com DOI); periódico, ano e acesso
  aberto = **OpenAlex**.
- **Métricas acadêmicas (citações, h-index):** seção removida do site em 04/10/2026.
  O OpenAlex fica defasado em relação ao Google Scholar, e o Scholar bloqueia (HTTP 403)
  os servidores do GitHub Actions, então não há fonte automática confiável.
- **Frequência:** todo dia às 09:00 UTC; também roda ao alterar o script/workflow
  e manualmente em Actions → Run workflow.
- **Commit:** só quando os dados mudam, como `github-actions[bot]`.
- **Token:** o `GITHUB_TOKEN` automático do Actions (nenhum segredo a configurar).

## 3. Google Analytics (GA4)

- Tag `G-DHC7T717QJ` (gtag.js) direto em `_layouts/default.html`.
- `analytics.provider` está `false` no `_config.yml` para não carregar o código
  antigo do Universal Analytics, que estava duplicado e obsoleto.

## 4. GitHub Pages

- Build automático ("pages build and deployment") a cada push em `master`.
