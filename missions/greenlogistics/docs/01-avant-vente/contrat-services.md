# Contrat de services managés

*Document fictif — scénario portfolio*

**Parties** : MB Data (prestataire) · GreenLogistics (client)

## Objet

Hébergement cloud privé souverain et services d'exploitation, d'industrialisation CI/CD et de modernisation du SI applicatif.

## Engagements

| Domaine | Engagement |
|---------|------------|
| Souveraineté | Données hébergées en France (datacenter Lyon), localisation transparente |
| Disponibilité | SLA 99,9 % sur la plateforme d'hébergement |
| Réversibilité | Export des données, restitution des manifests et infra-as-code, délai de transition 30 jours |
| Conformité | Traitement des données de géolocalisation et preuves de livraison selon exigences client |

## Responsabilités

| MB Data | GreenLogistics |
|---------|----------------|
| Plateforme K8s, réseau, observabilité | Code applicatif et évolutions métier |
| CI/CD, déploiements, sauvegardes plateforme | Validation recette et approbation MEP |
| Astreinte SRE, correctifs infrastructure | Accès aux environnements, tests fonctionnels |
| Mises à jour OS, K8s, opérateurs | Données métier et conformité RGPD interne |

## SLA incidents

| Priorité | Description | Prise en charge |
|----------|-------------|-----------------|
| P1 | Production indisponible | 15 min |
| P2 | Dégradation majeure | 1 h |
| P3 | Incident mineur | 4 h ouvrées |

## Conditions

- **Facturation** : abonnement mensuel fixe
- **Durée** : 36 mois, renouvelable
- **Maintenance** : fenêtre hebdomadaire planifiée (hors astreinte P1)

## Note lab portfolio

L'environnement de démonstration technique (OCI Always Free, région EU) est distinct du datacenter contractuel Lyon et n'impacte pas les engagements ci-dessus.
