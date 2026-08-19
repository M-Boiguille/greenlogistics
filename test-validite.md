# Rapport de test — Observabilité GreenLogistics

## Périmètre

Validation du déploiement de Prometheus, Grafana, Alertmanager, node-exporter et kube-state-metrics.

## Méthode

```bash
./deploy.sh
kubectl get pods -n monitoring
kubectl port-forward svc/prometheus 9090:9090 -n monitoring &
# Vérifier les targets : http://localhost:9090/targets
kubectl port-forward svc/grafana 3000:80 -n monitoring &
# Vérifier le dashboard : http://localhost:3000
# Vérifier l'ingress : curl -k -I https://grafana.greenlogistics.local
```

## Résultats

| Test | Commande | Résultat |
|------|----------|----------|
| Pods en Running | `kubectl get pods -n monitoring` | OK |
| Targets Prometheus | `curl -s localhost:9090/api/v1/targets` | OK |
| Dashboard Grafana | `curl -u admin:DemoPass123! localhost:3000/api/dashboards/uid/cluster-overview` | OK |
| Ingress HTTP 200 | `curl -k -I https://grafana.greenlogistics.local` | OK (après DNS) |
| Alertes visibles | `curl localhost:9090/api/v1/rules` | OK |

## Validation des critères d'acceptation

- [x] Prometheus déployé dans `monitoring` avec PVC.
- [x] node-exporter et kube-state-metrics collectés.
- [x] Règles d'alerte actives.
- [x] Grafana accessible via ingress TLS avec auth.
- [x] Dashboard "Cluster Overview" provisionné.
- [x] Déploiement reproductible via `deploy.sh`.

## Limites

- Certificat TLS self-signed.
- Test en local avec port-forward.
- Alertes non connectées à un webhook réel.
