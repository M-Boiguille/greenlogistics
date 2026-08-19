# Runbook — Observabilité GreenLogistics

## Objectif

Ce runbook documente le déploiement, l'exploitation et la mise à jour du socle Prometheus / Grafana / Alertmanager.

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
kubectl create secret generic grafana-admin -n monitoring --from-literal=password='VOTRE_MOT_DE_PASSE'
for f in manifests/*.yaml; do kubectl apply -f "$f"; done
```

## Mise à jour

1. Modifier le manifeste concerné.
2. Appliquer : `kubectl apply -f manifests/<fichier>.yaml`
3. Vérifier le rollout : `kubectl rollout status deployment/<nom> -n monitoring`

## Rollback

```bash
kubectl rollout undo deployment/<nom> -n monitoring
```

## Alertes configurées

- `HighCPU` : CPU > 80% pendant 5 minutes
- `PodDown` : pod en phase Failed ou Unknown
- `LowDiskSpace` : espace disque < 10%

## Dépannage

1. Vérifier les pods : `kubectl get pods -n monitoring`
2. Vérifier les targets Prometheus : `kubectl port-forward svc/prometheus 9090 -n monitoring`
3. Vérifier les alertes : `kubectl port-forward svc/alertmanager 9093 -n monitoring`
4. Vérifier le dashboard : `kubectl port-forward svc/grafana 3000:80 -n monitoring`
