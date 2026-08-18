# Synthèse environnement

*Document fictif — scénario portfolio*

**GreenLogistics** — Lab OCI Always Free

*Template à compléter par l'ingénieur DevOps après déploiement (phase 4).*

## Compute

| Attribut | Valeur |
|----------|--------|
| Fournisseur | OCI Always Free |
| Région | `eu-???-1` |
| Shape | VM.Standard.A1.Flex |
| OCPU / RAM | 3 / ~18 Go |
| OS | Debian 12 |

## Accès

| Usage | Méthode |
|-------|---------|
| Admin K8s | WireGuard → kubectl |
| SSH | Via VPN uniquement |
| Apps publiques | HTTPS via Traefik |

## URLs

| Service | URL |
|---------|-----|
| Portail | `https://portail.example.com` |
| API | `https://api.example.com` |
| ERP LogiSoft | `https://erp.example.com` |
| Status | `https://status.example.com` |

## Namespaces Kubernetes

| Namespace | Rôle |
|-----------|------|
| `greenlogistics-dev` | Déploiement auto |
| `greenlogistics-recette` | Validation manuelle |
| `greenlogistics-prod` | Démo publique |

## Comptes de service

| Compte | Usage |
|--------|-------|
| CI deploy | kubeconfig dédié (secret) |
| backup | pg_dump planifié |

> Ne jamais committer mots de passe ni kubeconfig.

## Référence

- [Cahier des charges plateforme](cahier-charges-plateforme.md)
