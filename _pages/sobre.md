---
permalink: /pt/
title: "Sobre"
seo_title: "Luis C. N. Santos | Pesquisador na UFSC | Dinâmica Quântica e Clássica"
description: "Luis C. N. Santos, pesquisador da Universidade Federal de Santa Catarina (UFSC), trabalha com dinâmica quântica e clássica em espaços-tempos curvos."
locale: "pt-BR"
translations:
  en: /
  pt-BR: /pt/
author_profile: true
redirect_from:
  - /sobre/
---

<p style="text-align:right"><a href="/" hreflang="en" lang="en">English version</a></p>

Sou físico teórico na [Universidade Federal de Santa Catarina (UFSC)](https://ufsc.br), especializado em **Relatividade Geral e Gravitação Modificada**. Minha pesquisa trata da dinâmica clássica e quântica de partículas em espaços-tempos curvos, com ênfase em buracos negros, estrutura de estrelas compactas e extensões da Relatividade Geral.

Na última década publiquei mais de 40 artigos em periódicos como *Physical Review D*, *European Physical Journal C*, *Classical and Quantum Gravity* e *Annals of Physics*. Também me interesso por Inteligência Artificial e suas aplicações à pesquisa científica e à análise de dados.

**Fique à vontade para entrar em contato para discussões ou colaborações.**

---

## Áreas de pesquisa

**Física de buracos negros** — Buracos negros de Kiselev, regulares e em rotação em gravitação modificada (f(R,T), Rastall, gravidade de Rainbow). Termodinâmica, sombras, análogos acústicos e a unificação Rastall-Rainbow.

**Estrelas compactas** — Estrelas de nêutrons, estrelas de quarks e protoestrelas de nêutrons em teorias estendidas da gravitação. Equações TOV e TOV generalizada, vínculos astrofísicos bayesianos, híperons e ressonâncias Δ, equações de estado.

**Mecânica quântica em espaço-tempo curvo** — Campos escalares e fermiônicos em espaços-tempos de cordas cósmicas, defeitos topológicos, universo de Melvin e efeitos não inerciais. Oscilador de Klein-Gordon em espaços-tempos não triviais.

**Gravitação modificada e estendida** — f(R,T), f(T,T), Rastall, gravidade de Rainbow e extensões em geometria de Finsler. Formulação teórica e assinaturas astrofísicas.

---

## Publicações recentes

{% if site.data.publications_sync %}
{% assign pubs = site.data.publications_sync.works | sort: "publication_date" | reverse %}
{% for pub in pubs limit:5 %}
- [{{ pub.title }}]({{ pub.doi }})  
  **{{ pub.journal }}** · {{ pub.year }}{% if pub.is_open_access %} · 🔓 Acesso aberto{% endif %}
{% endfor %}
{% endif %}

[→ Ver todas as publicações](/publications/)

---

## Equações que acho bonitas

**Equações de campo de Einstein**

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\, T_{\mu\nu}$$

O alicerce da Relatividade Geral: a geometria do espaço-tempo à esquerda, o conteúdo de matéria e energia à direita. Todo buraco negro e toda estrela compacta que estudo vivem dentro dessas equações.

**Equação de Tolman–Oppenheimer–Volkoff**

$$\frac{dP}{dr} = -\frac{(\varepsilon + P)(M + 4\pi r^3 P)}{r(r - 2M)}$$

A equação de estrutura estelar na Relatividade Geral completa — governa o interior de estrelas de nêutrons, estrelas de quarks e de todo objeto compacto que modelo. Uma correção relativística da hidrostática newtoniana que muda tudo em altas densidades.

**Equação de Klein–Gordon em espaço-tempo curvo**

$$\frac{1}{\sqrt{-g}}\, \partial_\mu \!\left(\sqrt{-g}\, g^{\mu\nu} \partial_\nu \Phi\right) - m^2 \Phi = 0$$

A equação de onda relativística mais simples, generalizada para qualquer fundo curvo. O ponto de partida de todo o meu trabalho sobre dinâmica quântica em espaços-tempos de cordas cósmicas, defeitos topológicos e gravidade de Rainbow.

**Equações de Maxwell (forma covariante)**

$$\nabla_\mu F^{\mu\nu} = J^\nu \qquad \nabla_{[\mu} F_{\nu\rho]} = 0$$

A formulação mais elegante do eletromagnetismo — duas equações que dizem tudo. O universo de Melvin, onde estudo campos carregados, é inteiramente construído a partir de soluções dessas equações.

---

## Novidades

- **2026** — Três artigos aceitos no *EPJC* e na *Physical Review D*; protoestrelas de nêutrons em rotação com híperons e ressonâncias Δ
- **2025** — Nove publicações em um único ano, em *PRD*, *CQG*, *EPJC*, *Annals of Physics* e *Universe*
- **2024** — Artigos sobre buracos negros regulares a partir do fluido de Kiselev e análise bayesiana de modelos de quarks no *EPJC* e na *PRD*
- **2023** — Estudos sobre estrelas de nêutrons em rotação rápida e efeitos quânticos não inerciais em fundos de gravitação modificada

---

## Colaborações

Estou aberto a colaborações em:
- Teorias de gravitação modificada e suas assinaturas astrofísicas
- Modelagem de estrelas compactas e vínculos sobre equações de estado
- Teoria quântica de campos em espaços-tempos curvos e topologicamente não triviais
- Aplicações de IA/aprendizado de máquina à física teórica e à análise de dados

[→ Entre em contato](/contact/)
