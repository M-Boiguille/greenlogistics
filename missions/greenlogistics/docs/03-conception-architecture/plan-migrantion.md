# Plan de migration

*Document fictif — scénario portfolio*

**GreenLogistics** — Bascule vers plateforme Kubernetes OCI

## Prérequis

- Cluster k3s OCI validé (smoke tests `/health` OK)
- Workflows GitHub Actions verts, images poussées sur GHCR
- Recette fonctionnelle signée par le métier
- WireGuard opérationnel pour l'administration

## Étapes

1. **Migration données** — Export MySQL, import PostgreSQL, validation intégrité
2. **Déploiement recette** — 3 apps + BDD (namespace `recette`), tests charge et scan vulnérabilités
3. **Go/No Go** — Comité de pilotage (DSI, Responsable IT, CTO MB Data)
4. **Bascule production** — Dimanche matin, salle de crise virtuelle
5. **Bascule DNS** — Pointage vers ingress Traefik, validation post-bascule

## Rétroplanning (2 semaines)

| Jour | Activité |
|------|----------|
| J-10 | Migration données en recette, tests intégrité |
| J-7 | Tests fonctionnels métier + tests de charge |
| J-3 | Go/No Go comité de pilotage |
| J-1 | Gel des déploiements, pg_dump BDD |
| J0 | Bascule DNS, `helm upgrade` prod, smoke tests |
| J+1 | Page de statut active, retour d'expérience |

## Rollback

- **Critères** : erreurs critiques métier, indisponibilité > 30 min, corruption données
- **DNS** : retour vers anciens serveurs physiques (TTL bas pré-configuré)
- **BDD** : restauration pg_dump pré-bascule
- **Apps** : `helm rollback` vers version N-1

## Check-list pré-bascule

- [ ] pg_dump BDD validé
- [ ] Rollback DNS testé
- [ ] WireGuard actif, accès admin vérifié
- [ ] Workflows GHA et images GHCR à jour
- [ ] Équipes MB Data + GreenLogistics en ligne
- [ ] Communication utilisateurs envoyée
