# Guide du développeur

*Document fictif — scénario portfolio*

**GreenLogistics** — Conventions pour contribuer au SI modernisé (phase 5)

*Document destiné au développeur GreenLogistics — rédigé par l'ingénieur DevOps MB Data.*

## Environnement local

| Besoin | Outil |
|--------|-------|
| Conteneurs | Docker |
| Accès cluster dev | kubeconfig fourni par MB Data (WireGuard) |
| Registry | GHCR — images `ghcr.io/<org>/greenlogistics-*` |

## Workflow de contribution

1. Fork / branche selon stratégie ([conventions](conventions.md))
2. Push → pipeline CI (lint, test, build image)
3. PR vers `main` — review Responsable IT
4. Merge → deploy auto en `dev`
5. `workflow_dispatch` pour recette puis prod

## Structure applicative (cible — à créer)

| App | Stack | Rôle |
|-----|-------|------|
| LogiSoft | PHP 8, Apache | ERP logistique (stub `/health`) |
| Portail | Static ou React | Portail client |
| API mobile | Node.js | API livraison |

> En lab portfolio : stubs minimaux avec endpoint `/health` — le métier ERP reste hors périmètre DevOps.

## Conventions commit

- Conventional Commits (`feat:`, `fix:`, `chore:`)
- Hook commitlint actif sur le repo

## Support

| Contact | Rôle |
|---------|------|
| Ingénieur DevOps MB Data | Pipelines, Helm, cluster |
| Responsable IT GreenLogistics | Validation recette |

## Références

- [Cahier des charges CI/CD](cahier-charges-cicd.md)
- [DAT](../03-conception-architecture/DAT.md)
