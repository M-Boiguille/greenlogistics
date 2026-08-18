# Mission greenlogistics-001 — Tracking sécurisé

Cette mission implémente l'exposition sécurisée de l'application de tracking via un Ingress TLS géré par cert-manager.

## Fichiers

- `namespace.yaml` : namespace greenlogistics
- `configmap.yaml` : variables de configuration
- `secret.yaml` : secret applicatif
- `deployment.yaml` : déploiement nginx
- `service.yaml` : service ClusterIP
- `cluster-issuer.yaml` : émetteur self-signed
- `certificate.yaml` : certificat TLS
- `ingress.yaml` : exposition HTTPS

## Déploiement

```bash
kubectl apply -f k8s/
```

## Tests

```bash
curl -k https://tracking.greenlogistics.local
kubectl get certificate -n greenlogistics
```
