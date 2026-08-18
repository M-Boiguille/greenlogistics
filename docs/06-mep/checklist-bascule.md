# Check-list bascule production

*Document fictif — scénario portfolio*

**GreenLogistics** — MEP lab OCI (phase 6)

Complément opérationnel du [plan de migration](../03-conception-architecture/plan-migrantion.md).

## J-7

- [ ] Recette signée ([PV](pv-recette.md))
- [ ] Images GHCR taguées version release
- [ ] pg_dump recette validé (restauration testée)

## J-1

- [ ] Gel des merges sur `main`
- [ ] Communication utilisateurs internes
- [ ] Snapshot BDD production (pg_dump)
- [ ] Rollback Helm N-1 testé sur recette
- [ ] TTL DNS abaissé si applicable

## J0 — bascule

- [ ] Pipeline de déploiement configuré (GitHub Actions)
- [ ] Smoke tests : portail, API, ERP `/health`
- [ ] Vérification logs Traefik / pods
- [ ] Page [status](../07-exploitation/status.md) verte

## J+1

- [ ] Monitoring renforcé 24 h
- [ ] Rétrospective courte (notes incident si applicable)
- [ ] [Rapport mensuel](rapport-mensuel-template.md) amorcé

## Rollback (si besoin)

1. `helm rollback` apps concernées
2. Restauration pg_dump J-1
3. Communication stakeholders
