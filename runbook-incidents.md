# Runbook d'incidents — Supervision GreenLogistics

## Objectif

Ce runbook guide les opérateurs pour détecter, qualifier et réagir aux incidents courants sur le cluster GreenLogistics grâce à Prometheus, Grafana et Alertmanager.

## Accès

| Service | URL | Port interne |
|---------|-----|--------------|
| Prometheus | http://prometheus.monitoring.svc:9090 | 9090 |
| Grafana | https://grafana.greenlogistics.local | 3000 |
| Alertmanager | http://alertmanager.monitoring.svc:9093 | 9093 |

## Identifiants Grafana

- Login : `admin`
- Mot de passe : `DemoPass123!`

## Déploiement de la stack

```bash
chmod +x deploy-monitoring.sh
./deploy-monitoring.sh
```

## Alertes configurées

- `HighCPU` : CPU > 80% pendant 5 minutes
- `PodDown` : pod en phase Failed ou Unknown
- `LowDiskSpace` : espace disque < 10%

## Réponse aux incidents

### HighCPU

1. Identifier le pod consommateur : `kubectl top pods -n <namespace>`
2. Vérifier les logs : `kubectl logs <pod> -n <namespace> --tail=100`
3. Si nécessaire, scaler horizontalement ou verticalement.
4. Si le pod est hors de contrôle : `kubectl delete pod <pod> -n <namespace>`

### PodDown

1. Lister les pods en échec : `kubectl get pods -n <namespace> --field-selector=status.phase!=Running`
2. Vérifier les événements : `kubectl describe pod <pod> -n <namespace>`
3. Vérifier les ressources et les limits.
4. Redémarrer ou rollback si nécessaire.

### LowDiskSpace

1. Identifier le nœud : `kubectl get nodes -o wide`
2. Vérifier l'utilisation disque : `df -h` sur le nœud.
3. Nettoyer les images Docker inutilisées : `crictl rmi --prune` ou `docker system prune`.

## Rollback

```bash
kubectl rollout undo deployment/<nom> -n monitoring
```

## Dépannage

- Vérifier les pods : `kubectl get pods -n monitoring`
- Vérifier les targets Prometheus : `kubectl port-forward svc/prometheus 9090 -n monitoring`
- Vérifier les alertes : `kubectl port-forward svc/alertmanager 9093 -n monitoring`
- Vérifier le dashboard : `kubectl port-forward svc/grafana 3000:80 -n monitoring`
