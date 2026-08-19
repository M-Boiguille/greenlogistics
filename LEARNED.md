# Ce que j'ai appris — Mission greenlogistics-001

## Objectif

Déployer le socle d'observabilité Prometheus / Grafana / Alertmanager pour GreenLogistics.

## Concepts connus renforcés

- Kubernetes Deployments, Services, ConfigMaps, Secrets, PVC
- DaemonSet pour un exporter par nœud
- RBAC (ServiceAccount, ClusterRole, ClusterRoleBinding)

## Nouvelles notions maîtrisées

- Prometheus scrape config et alerting rules
- Grafana dashboard provisioning via ConfigMap
- kube-state-metrics et son RBAC
- Stockage persistant pour Prometheus

## Choix techniques

- Prometheus avec stockage persistant (PVC) pour conserver l'historique.
- node-exporter en DaemonSet pour couvrir chaque nœud.
- kube-state-metrics avec RBAC minimal.
- Dashboards Grafana provisionnés en as-code.
- Secret admin Grafana créé manuellement, non versionné.

## Liens utilisés

- https://prometheus.io/docs/introduction/overview/
- https://grafana.com/docs/grafana/latest/dashboards/
- https://kubernetes.io/docs/reference/access-authn-authz/rbac/

## Erreurs et corrections

- Le secret Grafana contenait un mot de passe en clair ; corrigé par un manifeste vide + commande kubectl.
- Prometheus manquait de stockage persistant ; corrigé par un PVC et un montage dans /prometheus.
