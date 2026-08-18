# Cahier des charges — CI/CD

*Document fictif — scénario portfolio*

**Phase 5** — Intégration continue et déploiement (4 semaines) | MB Data × GreenLogistics

## Contexte (AI_STORY)

- **Intervenants** : Ingénieur DevOps MB Data, développeur GreenLogistics (validation recette)
- **Objectif** : conteneuriser les 3 apps, pipelines automatisés, déploiement Helm sur dev/recette/prod

## Périmètre lab OCI

| Domaine | À réaliser |
|---------|------------|
| Conteneurisation | Dockerfiles LogiSoft (PHP), portail (static), API (Node) — stubs `/health` |
| Registry | GitHub Container Registry (GHCR) |
| CI | GitHub Actions — lint, build, push image |
| CD | GitHub Actions — `helm upgrade` (manuel recette/prod) |
| Packaging | Charts Helm par application + PostgreSQL |
| Auth lab | JWT applicatif léger (Keycloak = cible Lyon uniquement) |

## Périmètre cible client Lyon (documentation)

- Forgejo + runners dédiés
- Charts Helm versionnés
- Keycloak intégré portail + API

## Décisions (AI_STORY)

| Sujet | Décision |
|-------|----------|
| Branches portail | trunk-based |
| Branches ERP | Gitflow |
| Recette / prod | déploiement manuel avec approbation |

## Livrables documentaires

- [Guide développeur](guide-developpeur.md)
- [Conventions](conventions.md)
- Documentation pipelines *(à rédiger dans ton repo après implémentation)*

## Livrables techniques (à coder)

- 3 Dockerfiles + stubs applicatifs minimaux
- Charts Helm : logisoft, portail, api-mobile, postgresql
- Workflows : validation statique, build-push, deploy
- Secrets GitHub : kubeconfig, registry

## Critères d'acceptation (Go)

- [ ] Push sur `main` déclenche build et push GHCR
- [ ] Deploy `dev` automatique, `recette`/`prod` sur approbation
- [ ] `helm lint` et tests smoke `/health` verts
- [ ] 3 apps accessibles via ingress HTTPS
- [ ] Guide développeur validé par le développeur GreenLogistics (fictif)

## Références

- [DAT](../03-conception-architecture/DAT.md) — flux CI/CD
- [Feuille de route](../02-audit/feuille-de-route.md) — M3
- [Rapport d'audit](../02-audit/rapport-audit.md) — décisions CI/CD
