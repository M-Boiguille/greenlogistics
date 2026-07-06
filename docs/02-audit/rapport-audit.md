# Rapport d'audit

*Document fictif — scénario portfolio*

**MB Data** → **GreenLogistics** | Audit approfondi — 2 semaines (ateliers sur site + analyse code)

## Applications

| Application | Techno | État |
|-------------|--------|------|
| LogiSoft (ERP) | PHP monolithique | Serveur physique, déploiement manuel |
| Portail client | React | Build artisanal, pas de pipeline |
| API mobile | Node.js | Couplée à l'ERP, pas de supervision |
| Bases de données | MySQL + PostgreSQL | Hétérogène, pas de stratégie unifiée |

## Constats

- Déploiements par FTP le vendredi soir, sans procédure de rollback
- Aucune supervision ni alerting sur les services critiques
- Pas de SSO : authentifications dispersées entre applications
- Scripts de build et de déploiement non versionnés
- Administration réseau non segmentée (accès direct aux serveurs)

## Décisions arbitrées

| Sujet | Décision |
|-------|----------|
| ERP LogiSoft | Conteneuriser sans réécriture (PHP-Apache + volume persistant) |
| Bases de données | Standardiser sur PostgreSQL, migrer les MySQL restantes |
| Administration | VPN WireGuard pour l'accès admin sécurisé |
| Portail client | Haute disponibilité + déploiement automatisé |
| Identité (prod client) | SSO via Keycloak (portail + API) |
| Identité (lab) | Auth JWT applicative (empreinte minimale OCI) |
| CI/CD (lab) | GitHub Actions + GHCR |

## Quick wins

- Mise en place de sauvegardes automatisées (pg_dump)
- Healthchecks `/health` sur chaque service
- VPN d'administration WireGuard

## Recommandations

- Industrialiser CI/CD : GitHub Actions + GHCR (lab) ; Forgejo (production souveraine)
- Conteneuriser les 3 applications avec Helm
- Page de statut publique pour supervision légère (phase 2)
- Observabilité complète Prometheus/Grafana en cible client Lyon
