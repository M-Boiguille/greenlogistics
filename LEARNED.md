# Ce que j'ai appris — Mission greenlogistics-001

## Objectif

Mise en place de la supervision et de l'alerting pour le SI GreenLogistics avec Prometheus, Grafana et Alertmanager.

## Concepts connus renforcés

- Kubernetes Deployments, Services, ConfigMaps, Secrets
- Ingress TLS avec cert-manager
- Namespace isolation

## Nouvelles notions maîtrisées

- Prometheus scrape config et alerting rules
- Grafana anonymous disabled + auth secret
- Alertmanager basic deployment

## Choix techniques

- Prometheus en vanilla plutôt qu'Helm pour maîtriser chaque composant.
- Grafana avec authentification obligatoire (pas d'accès anonyme).
- Alertmanager déployé séparément pour respecter l'architecture Prometheus.

## Liens utilisés

- https://prometheus.io/docs/prometheus/latest/querying/basics/
- https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
- https://grafana.com/docs/grafana/latest/getting-started/getting-started-prometheus/

## Erreurs et corrections

- L'alerte `PodDown` initialement mal formée a été corrigée avec `kube_pod_status_phase`.
- L'accès anonyme Grafana a été désactivé via `GF_AUTH_ANONYMOUS_ENABLED`.
