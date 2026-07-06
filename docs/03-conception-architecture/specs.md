# Spécifications des environnements

*Document fictif — scénario portfolio*

**GreenLogistics** — Dimensionnement lab OCI

## OCI Always Free (24/7)

| Ressource | Allocation |
|-----------|------------|
| VM Ampere | 3 OCPU, ~18 Go RAM, 150 Go disque |
| k3s + OS | ~1,5 Go RAM |
| PostgreSQL | 512 Mo RAM, 20 Go PVC |
| LogiSoft (ERP) | 384 Mo RAM, 10 Go PVC, 1 replica |
| Portail client | 256 Mo RAM, 1 replica |
| API mobile | 256 Mo RAM, 1 replica |
| WireGuard + Traefik | ~200 Mo RAM |
| **Marge disponible** | ~15 Go RAM, ~110 Go disque |

## Environnements (namespaces)

| Namespace | Ressources |
|-----------|------------|
| dev | Identiques, déploiement auto |
| recette | Identiques, déploiement manuel |
| prod | Identiques, déploiement manuel |

## Cible client production (référence — datacenter Lyon)

| Service | CPU | RAM | Stockage | Replicas |
|---------|-----|-----|----------|----------|
| Cluster (3 nœuds) | 4 vCPU × 3 | 16 Go × 3 | 200 Go/nœud | — |
| LogiSoft | 1/2 | 2/4 Go | 50 Go PVC | 1 |
| Portail | 0.5/1 | 512 Mo/1 Go | — | 2 |
| API mobile | 0.5/1 | 512 Mo/1 Go | — | 2 |
| PostgreSQL | 2/4 | 4/8 Go | 100 Go PVC | 1 |
| Keycloak | 0.5/1 | 1/2 Go | 10 Go | 1 |
| Prometheus/Grafana | 1/2 | 2/4 Go | 30 Go | 1 |

## Coût lab

| Poste | Coût |
|-------|------|
| OCI Always Free | 0 €/mois |
