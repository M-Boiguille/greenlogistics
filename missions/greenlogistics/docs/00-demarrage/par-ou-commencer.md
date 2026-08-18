# Par où commencer

*Document fictif — scénario portfolio*

Guide de lecture et ordre de travail pour l'ingénieur DevOps MB Data sur la mission GreenLogistics.

> **Ce dépôt documente la mission.** Le code (Terraform, Ansible, Helm, Dockerfiles, GitHub Actions) est **à implémenter par toi** — voir les cahiers des charges phases 4 à 7.

## Ordre de lecture (contexte mission)

| # | Phase | Documents |
|---|-------|-----------|
| 1 | Avant-vente | [Proposition](../01-avant-vente/proposition-commerciale.md), [Contrat](../01-avant-vente/contrat-services.md) |
| 2 | Audit | [Rapport](../02-audit/rapport-audit.md), [Feuille de route](../02-audit/feuille-de-route.md) |
| 3 | Conception | [DAT](../03-conception-architecture/DAT.md), [Specs](../03-conception-architecture/specs.md), [Migration](../03-conception-architecture/plan-migrantion.md) |
| 4 | Plateforme | [Cahier des charges](../04-plateforme/cahier-charges-plateforme.md) |
| 5 | CI/CD | [Cahier des charges](../05-cicd/cahier-charges-cicd.md), [Guide dev](../05-cicd/guide-developpeur.md) |
| 6 | MEP | [PV recette](../06-mep/pv-recette.md), [Checklist](../06-mep/checklist-bascule.md) |
| 7 | RUN | [Cahier des charges RUN](../07-exploitation/cahier-charges-run.md) |

## Ordre d'implémentation (ton travail)

| Étape | Objectif | Doc de référence |
|-------|----------|------------------|
| 1 | Comprendre l'architecture lab | DAT partie B |
| 2 | Provisionner OCI | Cahier des charges plateforme |
| 3 | k3s + WireGuard | Cahier des charges plateforme |
| 4 | Helm + PostgreSQL | Specs, DAT |
| 5 | Stubs apps + Docker | Cahier des charges CI/CD |
| 6 | Pipelines GHA | Cahier des charges CI/CD |
| 7 | Status + RUN | Cahier des charges RUN |

## Prérequis outils

Terraform · Ansible · kubectl · Helm · Docker · compte OCI Always Free · GitHub + GHCR

## Périmètre DevOps

- **In scope** : infra, charts, pipelines, runbooks, monitoring léger
- **Out of scope** : code métier ERP/portail — stubs `/health` uniquement

## Après chaque phase

Compléter les templates : [synthèse environnement](../04-plateforme/synthese-environnement.md), [rapport perf](../04-plateforme/rapport-tests-performance.md), [rapport mensuel](../07-exploitation/rapport-mensuel-template.md).
