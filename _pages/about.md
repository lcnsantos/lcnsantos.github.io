---
permalink: /
title: "About"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am a theoretical physicist at the [Federal University of Santa Catarina (UFSC)](https://ufsc.br), Brazil, specializing in **General Relativity and Modified Gravity**. My research focuses on the classical and quantum dynamics of particles in curved spacetime, with particular emphasis on black hole physics, compact star structure, and extensions of General Relativity.

Over the past decade I have published more than 40 papers in journals including *Physical Review D*, *European Physical Journal C*, *Classical and Quantum Gravity*, and *Annals of Physics*. I am also interested in Artificial Intelligence and its applications to scientific research and data analysis.

**Feel free to reach out for discussions or collaborations.**

---

## Research areas

**Black hole physics** — Kiselev, regular, and rotating black holes in modified gravity (f(R,T), Rastall, Rainbow gravity). Thermodynamics, shadows, acoustic analogues, and the Rastall-Rainbow unification.

**Compact stars** — Neutron stars, quark stars, and protoneutron stars in extended gravity theories. TOV and generalized TOV equations, Bayesian astrophysical constraints, hyperons and Δ resonances, equations of state.

**Quantum mechanics in curved spacetime** — Scalar and fermionic fields in cosmic string backgrounds, topological defects, Melvin universe, and non-inertial effects. Klein-Gordon oscillator in nontrivial spacetimes.

**Modified and extended gravity** — f(R,T), f(T,T), Rastall, Rainbow gravity, and Finsler geometry extensions. Theoretical formulation and astrophysical signatures.

---

## Recent publications

{% if site.data.publications_sync %}
{% assign pubs = site.data.publications_sync.works | sort: "publication_date" | reverse %}
{% for pub in pubs limit:5 %}
- [{{ pub.title }}]({{ pub.doi }})  
  **{{ pub.journal }}** · {{ pub.year }}{% if pub.cited_by_count > 0 %} · {{ pub.cited_by_count }} citations{% endif %}{% if pub.is_open_access %} · 🔓 Open Access{% endif %}
{% endfor %}
{% else %}
- [Scalar bosons with Coulomb potentials in a space with dual topological defects in rainbow gravity](https://doi.org/10.1140/epjc/s10052-026-15630-2)  
  **European Physical Journal C** · 2026
- [Kiselev black strings in f(R, T) gravity](https://doi.org/10.1140/epjc/s10052-026-15503-8)  
  **European Physical Journal C** · 2026
- [Hyperons and Δ's in rotating protoneutron stars: local properties](https://doi.org/10.1103/7wsg-k9t6)  
  **Physical Review D** · 2026
- [Strongly interacting quark matter in massive quark stars](https://doi.org/10.1088/1361-6382/ade192)  
  **Classical and Quantum Gravity** · 2025
- [Revisiting black holes surrounded by cloud and fluid of strings in general relativity](https://doi.org/10.1103/PhysRevD.111.064032)  
  **Physical Review D** · 2025
{% endif %}

[→ View all publications](/publications/)

---

## Academic metrics

{% if site.data.metrics %}
{% assign m = site.data.metrics.summary %}

| | |
|---|---|
| Publications | **{{ m.works_count }}** |
| Total citations | **{{ m.cited_by_count }}** |
| h-index | **{{ m.h_index }}** |
| i10-index | **{{ m.i10_index }}** |

_Updated {{ site.data.metrics.updated | date: "%B %Y" }} via [OpenAlex](https://openalex.org/authors/https://orcid.org/0000-0002-6129-1820)_

{% else %}
_Metrics loaded automatically via GitHub Actions weekly._  
[Google Scholar profile](https://scholar.google.com.br/citations?user=KorU-HsAAAAJ&hl=pt-BR) · [ORCID 0000-0002-6129-1820](https://orcid.org/0000-0002-6129-1820)
{% endif %}

---

## Equations I find beautiful

**Einstein field equations**

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\, T_{\mu\nu}$$

The foundation of General Relativity: spacetime geometry on the left, energy-matter content on the right. Every black hole and every compact star I study lives inside these equations.

**Tolman–Oppenheimer–Volkoff equation**

$$\frac{dP}{dr} = -\frac{(\varepsilon + P)(M + 4\pi r^3 P)}{r(r - 2M)}$$

The stellar structure equation in full GR — governs the interior of neutron stars, quark stars, and every compact object I model. A relativistic correction to Newtonian hydrostatics that changes everything at high densities.

**Klein–Gordon equation in curved spacetime**

$$\frac{1}{\sqrt{-g}}\, \partial_\mu \!\left(\sqrt{-g}\, g^{\mu\nu} \partial_\nu \Phi\right) - m^2 \Phi = 0$$

The simplest relativistic wave equation generalized to any curved background. The starting point for all my work on quantum dynamics in cosmic string spacetimes, topological defects, and Rainbow gravity.

**Maxwell's equations (covariant form)**

$$\nabla_\mu F^{\mu\nu} = J^\nu \qquad \nabla_{[\mu} F_{\nu\rho]} = 0$$

The most elegant formulation of electromagnetism — two equations that say everything. The Melvin universe, where I study charged fields, is entirely built from solutions to these.

---

## News

- **2026** — Three papers accepted in *EPJC* and *Physical Review D*; rotating protoneutron stars with hyperons and Δ resonances
- **2025** — Nine publications in a single year across *PRD*, *CQG*, *EPJC*, *Annals of Physics*, and *Universe*
- **2024** — Papers on regular black holes from Kiselev fluid and Bayesian analysis of quark models in *EPJC* and *PRD*
- **2023** — Studies on rapidly rotating neutron stars and non-inertial quantum effects in modified gravity backgrounds

---

## Collaborate

I am open to collaborations in:
- Modified gravity theories and their astrophysical signatures
- Compact star modeling and equation-of-state constraints
- Quantum field theory in curved and topologically nontrivial spacetimes
- AI/ML applications to theoretical physics and data analysis

[→ Contact me](/contact/)
