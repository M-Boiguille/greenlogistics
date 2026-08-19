# Runbook — Supervision GreenLogistics

## Objectif

Ce runbook documente le déploiement et l'exploitation de la stack de supervision Prometheus / Grafana / Alertmanager.

## Accès

| Service | URL | Port interne |
|---------|-----|--------------|
| Prometheus | http://prometheus.monitoring.svc:9090 | 9090 |
| Grafana | https://grafana.greenlogistics.local | 3000 |
| Alertmanager | http://alertmanager.monitoring.svc:9093 | 9093 |

## Identifiants Grafana

- Login : `admin`
- Mot de passe : dans le secret `grafana-admin` du namespace `monitoring`

## Déploiement

```bash
kubectl apply -f manifests/namespace.yaml
kubectl apply -f manifests/prometheus-config.yaml
kubectl apply -f manifests/prometheus-alerts.yaml
kubectl apply -f manifests/prometheus-deployment.yaml
kubectl apply -f manifests/prometheus-service.yaml
kubectl apply -f manifests/grafana-secret.yaml
kubectl apply -f manifests/grafana-deployment.yaml
kubectl apply -f manifests/grafana-service.yaml
kubectl apply -f manifests/grafana-ingress.yaml
kubectl apply -f manifests/alertmanager-deployment.yaml
kubectl apply -f manifests/alertmanager-service.yaml
```

## Alertes configurées

- `HighCPU` : CPU > 80% pendant 5 minutes
- `PodDown` : pod en phase Failed ou Unknown
- `LowDiskSpace` : espace disque < 10%

## Dépannage

1. Vérifier les pods : `kubectl get pods -n monitoring`
2. Vérifier les targets Prometheus : `kubectl port-forward svc/prometheus 9090 -n monitoring`
3. Vérifier les alertes : `kubectl port-forward svc/alertmanager 9093 -n monitoring`
