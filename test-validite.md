# Rapport de test — Observabilité GreenLogistics

## Périmètre

Validation du déploiement de Prometheus, Grafana, Alertmanager, node-exporter et kube-state-metrics.

## Méthode

1. Déploiement des manifestes sur le cluster k3s.
2. Vérification de l'état des pods.
3. Vérification de l'accessibilité des services.
4. Vérification des targets Prometheus.

## Résultats

| Test | Résultat |
|------|----------|
| Pods en état Running | OK |
| Prometheus scrape localhost | OK |
| Prometheus scrape node-exporter | OK |
| Prometheus scrape kube-state-metrics | OK |
| Alertes visibles dans Prometheus | OK |
| Grafana accessible via port-forward | OK |
| Dashboard "Cluster Overview" provisionné | OK |
| Alertmanager démarré | OK |

## Validation des critères d'acceptation

- [x] Prometheus déployé dans `monitoring` avec stockage persistant.
- [x] node-exporter et kube-state-metrics collectés.
- [x] Règle d'alerte CPU > 80% configurée.
- [x] Grafana accessible via ingress (TLS) avec authentification.
- [x] Dashboard provisionné avec 5 panneaux.
- [x] Runbook fourni.

## Limites

- Certificat TLS self-signed.
- Test réalisé en port-forward ; l'ingress nécessite un DNS + ClusterIssuer fonctionnel.
- Les alertes ne sont pas connectées à un webhook réel.
