# Mission GreenLogistics

**Cloud Privé Souverain & Transformation DevOps**

Scénario fictif d'un ERP modernisé par une chaîne CI/CD, pour démontrer la transformation d'un SI legacy en plateforme cloud-native opérée.

## Contexte

GreenLogistics, PME de 250 salariés, souhaitait moderniser son SI logistique sans dépendre d'un hyperscaler américain. MB Data a été retenue pour fournir une plateforme cloud privée opérée et une industrialisation CI/CD.

> **Ce dépôt** = récit client (docs phases 1–3) + **lab portfolio** hébergé sur **OCI Always Free** (région EU, 24/7).

## Déroulé de la mission

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

### Phase 4 : Exploitation (lab)
- [Page de statut](docs/04-exploitation/status.md) *(à implémenter)*

### Mon rôle d'Ingénieur DevOps

En tant qu'ingénieur exploitation chez MB Data, j'ai pris en charge les **phases 4 à 7** : déploiement de la plateforme, automatisation CI/CD, mise en production et exploitation. L'infrastructure est codée, versionnée et documentée dans ce repo GitHub.

## Stack technique (lab OCI)

| Composant | Choix |
|-----------|-------|
| Cloud | OCI Always Free — VM Ampere, région EU |
| Orchestration | k3s single-node |
| Apps | LogiSoft (PHP), portail React, API Node.js |
| BDD | PostgreSQL |
| CI/CD | GitHub Actions → GHCR → Helm |
| Réseau | Traefik, cert-manager, WireGuard |
| Supervision | Endpoints `/health`, [page de statut](docs/04-exploitation/status.md) |

*Architecture cible client (datacenter Lyon) : voir [DAT](docs/03-conception-architecture/DAT.md) partie A.*

## Roadmap implémentation

| # | Phase | Contenu |
|---|-------|---------|
| 1 | **OCI** | k3s, apps, PostgreSQL, WireGuard, pipelines GHA |
| 2 | **Status** | Uptime Kuma ou UptimeRobot, badges site perso |
| 3 | *hors scope public* | — |

## Démo live

| Composant | Disponibilité |
|-----------|---------------|
| Applications GreenLogistics | **24/7** — URL publique OCI |
| Page de statut | **À venir** — phase 2 |
| Coût infrastructure | **0 €/mois** (OCI Always Free) |

## Mapping compétences

| Compétence | Où la trouver |
|------------|---------------|
| Kubernetes | k3s OCI — [DAT](docs/03-conception-architecture/DAT.md) |
| Terraform / Ansible / Helm | `infra/` *(à venir)* — [feuille de route](docs/02-audit/feuille-de-route.md) |
| PostgreSQL | Cluster OCI — [specs](docs/03-conception-architecture/specs.md) |
| WireGuard | VM OCI — [DAT](docs/03-conception-architecture/DAT.md) |
| CI/CD | GitHub Actions — `.github/workflows/` |
| Exploitation / monitoring | [status](docs/04-exploitation/status.md) |
