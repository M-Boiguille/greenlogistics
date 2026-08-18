# Procès-verbal de recette

*Document fictif — scénario portfolio*

**GreenLogistics** × **MB Data** — Recette lab OCI (phase 6)

## Informations

| Champ | Valeur |
|-------|--------|
| Date | *(à compléter)* |
| Environnement | `greenlogistics-recette` |
| Version déployée | `sha-________` |

## Tests réalisés

| # | Test | Résultat | Observations |
|---|------|----------|--------------|
| 1 | Accès portail HTTPS | OK / KO | |
| 2 | API `/health` | OK / KO | |
| 3 | ERP LogiSoft login | OK / KO | stub |
| 4 | Persistance PostgreSQL | OK / KO | |
| 5 | Rollback Helm N-1 | OK / KO | |
| 6 | Scan vulnérabilités images | OK / KO | |

## Charge (synthèse)

- Test k6 léger : ___ req/s, latence p95 ___ ms
- Ressources OCI dans les limites [specs](../03-conception-architecture/specs.md)

## Décision

- [ ] **Go** mise en production
- [ ] **No Go** — corrections requises : ___

## Signatures (fictives)

| Rôle | Nom | Date |
|------|-----|------|
| Responsable IT GreenLogistics | | |
| Ingénieur DevOps MB Data | | |
