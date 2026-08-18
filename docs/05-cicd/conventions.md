# Conventions CI/CD

*Document fictif — scénario portfolio*

**GreenLogistics** — Bonnes pratiques Ops (phase 5)

## Branches

| App | Stratégie |
|-----|-----------|
| Portail, API | trunk-based — push `main` → build |
| LogiSoft ERP | Gitflow light — `develop` + tags release |

## Commits

- Conventional Commits — hook commitlint sur le repo
- Exemples : `feat(helm): add postgresql chart`, `fix(ci): docker build api`

## Pull requests

- CI verte avant merge
- Review Responsable IT GreenLogistics (fictif)

## Déploiement par environnement

| Env | Déclenchement | Approbation |
|-----|---------------|-------------|
| dev | automatique sur merge | non |
| recette | manuel | Responsable IT |
| prod | manuel | DSI |

## Secrets

Stockage : GitHub Secrets ou équivalent — jamais dans le dépôt.

| Secret | Usage |
|--------|-------|
| Kubeconfig | Deploy Helm |
| OCI API | Terraform (optionnel CI) |

## Images

- Tag avec SHA du commit
- Éviter `:latest` seul en production

## Références

- [Cahier des charges CI/CD](cahier-charges-cicd.md)
- [Guide développeur](guide-developpeur.md)
