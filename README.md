# Mission GreenLogistics

**Cloud Privé Souverain & Transformation DevOps**

Scénario fictif d'un ERP modernisé par une chaîne CI/CD, pour démontrer la transformation d'un SI legacy en plateforme cloud-native opérée.

> **Ce dépôt documente la mission** (phases 1 à 7). L'implémentation infra/CI/CD est le travail de l'ingénieur DevOps — voir [Par où commencer](docs/00-demarrage/par-ou-commencer.md).

## Contexte

GreenLogistics, PME de 250 salariés, souhaitait moderniser son SI logistique sans dépendre d'un hyperscaler américain. MB Data a été retenue pour fournir une plateforme cloud privée opérée et une industrialisation CI/CD.

Lab portfolio : **OCI Always Free** (région EU, 24/7) — architecture dans le [DAT](docs/03-conception-architecture/DAT.md) partie B.

## Documentation mission

### Phase 1 : Avant-vente et contractualisation
- [Proposition commerciale](docs/01-avant-vente/proposition-commerciale.md)
- [Contrat de services](docs/01-avant-vente/contrat-services.md)

### Phase 2 : Audit approfondi
- [Rapport d'audit](docs/02-audit/rapport-audit.md)
- [Feuille de route](docs/02-audit/feuille-de-route.md)

### Phase 3 : Conception et architecture cible
- [Dossier d'Architecture Technique (DAT)](docs/03-conception-architecture/DAT.md)
- [Plan de migration](docs/03-conception-architecture/plan-migrantion.md)
- [Spécifications des environnements](docs/03-conception-architecture/specs.md)

### Phase 4 : Plateforme d'hébergement
- [Cahier des charges plateforme](docs/04-plateforme/cahier-charges-plateforme.md)
- [Synthèse environnement](docs/04-plateforme/synthese-environnement.md) *(template)*
- [Rapport tests performance](docs/04-plateforme/rapport-tests-performance.md) *(template)*

### Phase 5 : CI/CD
- [Cahier des charges CI/CD](docs/05-cicd/cahier-charges-cicd.md)
- [Guide développeur](docs/05-cicd/guide-developpeur.md)
- [Conventions](docs/05-cicd/conventions.md)

### Phase 6 : Recette et mise en production
- [PV de recette](docs/06-mep/pv-recette.md)
- [Check-list bascule](docs/06-mep/checklist-bascule.md)
- [Fiche fin de projet](docs/06-mep/fiche-fin-projet.md)

### Phase 7 : Exploitation (RUN)
- [Cahier des charges RUN](docs/07-exploitation/cahier-charges-run.md)
- [Page de statut](docs/07-exploitation/status.md)
- [Runbook incidents](docs/07-exploitation/runbook-incidents.md)
- [Template rapport mensuel](docs/07-exploitation/rapport-mensuel-template.md)

## Mon rôle d'Ingénieur DevOps

En tant qu'ingénieur exploitation chez MB Data, j'ai pris en charge les **phases 4 à 7** : plateforme, CI/CD, MEP et RUN. Les cahiers des charges décrivent ce que j'implémente sur le lab OCI.

## Stack technique (lab OCI — cible)

| Composant | Choix |
|-----------|-------|
| Cloud | OCI Always Free — VM Ampere, région EU |
| Orchestration | k3s single-node |
| Apps | LogiSoft (PHP), portail, API Node — stubs |
| BDD | PostgreSQL |
| CI/CD | GitHub Actions → GHCR → Helm |
| Réseau | Traefik, cert-manager, WireGuard |
| Supervision | `/health`, page de statut |

*Architecture cible client (datacenter Lyon) : [DAT](docs/03-conception-architecture/DAT.md) partie A.*

## Démo live

| Composant | Statut |
|-----------|--------|
| Documentation mission | Disponible (ce repo) |
| Lab OCI déployé | À implémenter (phases 4–7) |
| Coût cible | 0 €/mois (OCI Always Free) |

## Par où commencer

[Lire la documentation](docs/00-demarrage/par-ou-commencer.md) puis suivre les cahiers des charges phase 4 → 7.
