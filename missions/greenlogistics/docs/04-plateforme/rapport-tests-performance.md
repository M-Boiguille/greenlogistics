# Rapport — tests de performance initiaux

*Document fictif — scénario portfolio*

**GreenLogistics** — Validation dimensionnement lab OCI (phase 4)

## Contexte

Tests préliminaires avant industrialisation CI/CD, conformément à la phase 4 AI_STORY.

## Environnement testé

| Attribut | Valeur |
|----------|--------|
| Cluster | k3s single-node OCI |
| OCPU / RAM | 3 / ~18 Go |
| Outil charge | k6 ou équivalent *(à renseigner)* |
| Date | *(à compléter)* |

## Scénarios

| Scénario | Cible | Résultat | OK / KO |
|----------|-------|----------|---------|
| Smoke — 10 users, 1 min | Latence p95 < 500 ms | | |
| Charge — 50 users, 5 min | CPU < 80 %, pas d'OOM | | |
| Stress — montée progressive | Identification seuil | | |

## Synthèse

| Indicateur | Valeur mesurée | Seuil specs |
|------------|----------------|-------------|
| CPU max | ___ % | 80 % |
| RAM max | ___ % | 85 % |
| Requêtes/s max | ___ | — |

## Recommandations

- [ ] Ajuster limits Helm si nécessaire
- [ ] Valider marge disque PostgreSQL
- [ ] Documenter dans [specs](../03-conception-architecture/specs.md) si écart

## Décision

- [ ] **Go** — dimensionnement validé pour phase CI/CD
- [ ] **Ajustement requis** — détail : ___

*À compléter après tes tests sur le lab déployé.*
