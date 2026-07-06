# Feuille de route de modernisation

*Document fictif — scénario portfolio*

**Durée** : 4 mois | **Client** : GreenLogistics | **Prestataire** : MB Data

## Planning

| Mois | Phase | Livrables clés |
|------|-------|----------------|
| M1 | Conception + plateforme OCI | DAT, specs, Terraform OCI, k3s |
| M2 | Apps + CI/CD | Déploiement apps, WireGuard, workflows GitHub Actions |
| M3 | Recette + status | Helm prod/recette, page de statut publique |
| M4 | MEP + RUN | Bascule production, PV recette, exploitation |

## Jalons (critères Go)

| Jalon | Critère de validation |
|-------|----------------------|
| Fin M1 | DAT validé, VM OCI provisionnée, cluster k3s opérationnel |
| Fin M2 | 3 apps déployées, WireGuard actif, pipelines GHA verts |
| Fin M3 | Recette validée, page de statut en ligne |
| Fin M4 | Production basculée sur OCI, RUN documenté |

## Backlog initial (GitHub)

- Conteneuriser LogiSoft (Dockerfile PHP-Apache + PVC)
- Workflow GHA portail React (lint, test, build image, push GHCR)
- Workflow GHA API mobile Node.js
- Charts Helm par application + workflow deploy Helm
- Migration MySQL → PostgreSQL
- Page de statut (Uptime Kuma ou UptimeRobot)

## Risques

| Risque | Mitigation |
|--------|------------|
| Régression ERP à la conteneurisation | Tests de non-régression, recette métier prolongée |
| Bascule DNS | Fenêtre dimanche, rollback DNS préparé |
| Montée de charge portail | Tests de charge en recette, ajustement ressources OCI |

## Équipe projet

| MB Data | GreenLogistics |
|---------|----------------|
| Architecte DevOps, SRE, Ingénieur DevOps | DSI, Responsable IT, Développeur |
