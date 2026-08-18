# Mission greenlogistics-001 — Tracking sécurisé

Cette mission implémente l'exposition sécurisée de l'application de tracking via un Ingress TLS géré par cert-manager.

## Fichiers

- `namespace.yaml` : namespace greenlogistics
- `resourcequota.yaml` : quotas du namespace
- `configmap.yaml` : variables de configuration
- `html-configmap.yaml` : page HTML par défaut
- `secret.yaml` : secret applicatif
- `deployment.yaml` : déploiement nginx avec image alpine
- `service.yaml` : service ClusterIP
- `cert-manager-setup.yaml` : namespace cert-manager
- `cluster-issuer.yaml` : émetteur self-signed
- `certificate.yaml` : certificat TLS
- `ingress.yaml` : exposition HTTPS

## Prérequis

cert-manager doit être installé avant d'appliquer les ressources GreenLogistics :

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.14.0/cert-manager.yaml
kubectl wait --for=condition=Available deployment/cert-manager -n cert-manager --timeout=120s
```

## Déploiement

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/resourcequota.yaml
kubectl apply -f k8s/
```

## Rolling update

```bash
kubectl set image deployment/tracking-api nginx=nginx:alpine -n greenlogistics
kubectl rollout status deployment/tracking-api -n greenlogistics
```

## Tests

```bash
curl -k https://tracking.greenlogistics.local
kubectl get certificate -n greenlogistics
```
