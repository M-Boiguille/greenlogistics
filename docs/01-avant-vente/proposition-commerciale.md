# Proposition commerciale et technique

*Document fictif — scénario portfolio*

**MB Data** → **GreenLogistics** | Modernisation SI logistique & cloud privé souverain

## Client

- PME 250 salariés, logistique verte et traçabilité des flux
- SI on-premise (serveurs physiques au siège), équipe IT de 4 personnes
- Applications : ERP LogiSoft (PHP), portail client (React), API mobile (Node.js)
- Aucune expertise DevOps, Kubernetes ou CI/CD en interne

## Besoin

Moderniser le SI sans dépendre d'un hyperscaler américain : hébergement en France, déploiements automatisés, haute disponibilité du portail, SSO.

## Offre MB Data

Plateforme cloud privée **opérée** + forfait d'intégration pour la modernisation CI/CD. Abonnement mensuel fixe sur ressources réservées.

## Pourquoi MB Data

| Argument | Valeur |
|----------|--------|
| Souveraineté | Données en France, datacenter lyonnais, engagement contractuel |
| Accompagnement | Architecte DevOps dédié, pas de recrutement interne |
| Plateforme opérée | Hébergement + modernisation + exploitation des applications |
| Coûts prévisibles | Forfait fixe, stack 100 % open source, réversibilité |
| Innovation | GitOps, observabilité eBPF, sécurité — sans être cobaye |

## Stack technique (cible client)

KVM/Proxmox · kubeadm · Terraform · Ansible · Helm · Keycloak · WireGuard · Prometheus/Grafana · Forgejo

## Périmètre

1. Audit approfondi
2. Conception architecture cible
3. Déploiement plateforme d'hébergement
4. Industrialisation CI/CD
5. Recette et mise en production
6. Exploitation continue (RUN)

## Planning & SLA

- **Durée modernisation** : 4 mois
- **SLA plateforme** : 99,9 % de disponibilité
- **Prochaine étape** : signature du contrat de services, lancement de l'audit

## Lab portfolio

Démonstration technique de ce dépôt GitHub :

- **OCI Always Free** (24/7, région EU) : k3s, applications, PostgreSQL, WireGuard
- **CI/CD** : GitHub Actions, GHCR, Helm
- **Supervision** : page de statut publique *(phase 2)*
