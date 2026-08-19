# Documentation ops — Observabilité GreenLogistics

## Vue d'ensemble

Cette mission déploie Prometheus, Grafana et Alertmanager dans le namespace `monitoring` du cluster k3s single-node de GreenLogistics.

## Architecture

| Composant | Rôle | Exposition |
|-----------|------|------------|
| Prometheus | Collecte des métriques | ClusterIP |
| Grafana | Visualisation | Ingress TLS |
| Alertmanager | Gestion des alertes | ClusterIP |
| node-exporter | Métriques nœuds | DaemonSet + Service |
| kube-state-metrics | Métriques objets K8s | Deployment + Service |

## Dossiers

- `manifests-observabilite/` : tous les manifestes Kubernetes
- `deploy-monitoring.sh` : script de déploiement ordonné
- `runbook-incidents.md` : procédures d'intervention
- `LEARNED.md` : apprentissages de la mission

## Procédure de test

```bash
./deploy-monitoring.sh
kubectl get pods -n monitoring
kubectl port-forward svc/prometheus 9090:9090 -n monitoring
# http://localhost:9090/targets
kubectl port-forward svc/grafana 3000:80 -n monitoring
# http://localhost:3000 / admin / DemoPass123!
```

## Résultats attendus

- Targets Prometheus : `prometheus`, `node-exporter`, `kube-state-metrics`.
- Dashboards : Cluster Overview (5 panneaux).
- Alertes : HighCPU, PodDown, LowDiskSpace actives.
