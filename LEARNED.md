# Ce que j'ai appris — Mission greenlogistics-002

## Objectif

Déployer le socle d'observabilité Prometheus / Grafana / Alertmanager pour GreenLogistics, avec des runbooks d'incidents et une documentation ops.

## Concepts connus renforcés

- Kubernetes Deployments, Services, ConfigMaps, Secrets, PVC
- DaemonSet et Service pour node-exporter
- RBAC pour kube-state-metrics
- Ingress TLS avec cert-manager

## Nouvelles notions maîtrisées

- Prometheus scrape config et alerting rules
- Provisioning Grafana (datasource + dashboards)
- kube-state-metrics et node-exporter
- Stockage persistant pour Prometheus

## Choix techniques

- `manifests-observabilite/` pour isoler les livrables.
- `deploy-monitoring.sh` pour garantir l'ordre d'application.
- Prometheus avec PVC pour l'historique.
- Grafana provisionné en as-code pour la reproductibilité.

## Liens utilisés

- https://prometheus.io/docs/introduction/overview/
- https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
- https://grafana.com/docs/grafana/latest/dashboards/

## Erreurs et corrections

- Le premier secret Grafana contenait un mot de passe en clair ; corrigé par encodage base64.
- Le dashboard Grafana manquait de datasource ; corrigé par un ConfigMap `grafana-datasource`.
- Le ClusterIssuer était manquant ; ajouté pour le TLS.
