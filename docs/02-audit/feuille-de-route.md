# Feuille de route de modernisation

*Document fictif — scénario portfolio*

**Durée** : 4 mois | **Client** : GreenLogistics | **Prestataire** : MB Data

## Planning

| Mois | Phase | Livrables clés |
|------|-------|----------------|
| M1 | Conception + plateforme | DAT, specs, début Terraform OCI / Ansible |
| M2 | Plateforme opérationnelle | k3s, WireGuard, synthèse environnement |
| M3 | CI/CD + recette | Dockerfiles, Helm, GitHub Actions, deploy recette |
| M4 | MEP + RUN | Bascule prod, PV recette, exploitation |

## Jalons (critères Go)

| Jalon | Critère de validation |
|-------|----------------------|
| Fin M1 | DAT validé, VM OCI provisionnée *(par toi)* |
| Fin M2 | k3s opérationnel, WireGuard actif, synthèse remplie |
| Fin M3 | 3 apps en recette, pipelines CI configurés |
| Fin M4 | Production basculée, RUN documenté |

## Backlog initial (actions DevOps)

- [ ] Terraform OCI — VM, réseau, disque
- [ ] Ansible — k3s, WireGuard, durcissement
- [ ] Charts Helm — PostgreSQL, apps
- [ ] Dockerfiles stubs — LogiSoft, portail, API
- [ ] Workflows GitHub Actions — build, deploy
- [ ] Migration MySQL → PostgreSQL
- [ ] Page de statut publique

## Risques

| Risque | Mitigation |
|--------|------------|
| Régression ERP | Tests non-régression, recette prolongée |
| Bascule DNS | Fenêtre dimanche, rollback DNS préparé |
| Montée de charge | Tests charge — [rapport perf](../04-plateforme/rapport-tests-performance.md) |

## Équipe projet

| MB Data | GreenLogistics |
|---------|----------------|
| Architecte DevOps, SRE, Ingénieur DevOps | DSI, Responsable IT, Développeur |

## Références

- [Cahier des charges plateforme](../04-plateforme/cahier-charges-plateforme.md)
- [Cahier des charges CI/CD](../05-cicd/cahier-charges-cicd.md)
