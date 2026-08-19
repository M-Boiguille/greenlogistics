# Rapport de test — Supervision GreenLogistics

## Périmètre

Validation du déploiement de Prometheus, Grafana et Alertmanager.

## Méthode

1. Déploiement des manifestes sur le cluster k3s.
2. Vérification de l'état des pods.
3. Vérification de l'accessibilité des services.
4. Simulation d'une alerte (LowDiskSpace).

## Résultats

| Test | Résultat |
|------|----------|
| Pods en état Running | OK |
| Prometheus scrape localhost | OK |
| Alertes visibles dans Prometheus | OK |
| Grafana accessible via port-forward | OK |
| Alertmanager démarré | OK |

## Limites

- Le test a été effectué en local avec port-forward.
- Le certificat TLS est self-signed.
- Les alertes ne sont pas connectées à un webhook réel.

## Prochaines étapes

- Connecter Alertmanager à un webhook (Slack / PagerDuty).
- Créer un dashboard Grafana avec 5 panneaux.
- Ajouter node-exporter et kube-state-metrics.
