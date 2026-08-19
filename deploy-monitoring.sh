#!/bin/bash
set -e

echo "Création du namespace..."
kubectl apply -f manifests-observabilite/namespace.yaml

echo "Création du PVC, configmaps et secret..."
kubectl apply -f manifests-observabilite/prometheus-pvc.yaml
kubectl apply -f manifests-observabilite/prometheus-config.yaml
kubectl apply -f manifests-observabilite/prometheus-alerts.yaml
kubectl apply -f manifests-observabilite/grafana-secret.yaml

# Le secret Grafana est vide dans Git pour éviter toute fuite de credentials.
# Cette commande l'injecte au déploiement. En production, utiliser Sealed Secrets,
# SOPS, Vault ou External Secrets Operator.
GRAFANA_PASSWORD="${GRAFANA_PASSWORD:-DemoPass123!}"
kubectl create secret generic grafana-admin \
  -n monitoring \
  --from-literal=password="$GRAFANA_PASSWORD" \
  --dry-run=client -o yaml | kubectl apply -f -

echo "Création du ClusterIssuer..."
kubectl apply -f manifests-observabilite/cluster-issuer.yaml

echo "Déploiement RBAC et exporters..."
kubectl apply -f manifests-observabilite/kube-state-metrics-rbac.yaml
kubectl apply -f manifests-observabilite/kube-state-metrics-deployment.yaml
kubectl apply -f manifests-observabilite/kube-state-metrics-service.yaml
kubectl apply -f manifests-observabilite/node-exporter-ds.yaml
kubectl apply -f manifests-observabilite/node-exporter-service.yaml

echo "Déploiement Prometheus, Grafana et Alertmanager..."
kubectl apply -f manifests-observabilite/prometheus-deployment.yaml
kubectl apply -f manifests-observabilite/prometheus-service.yaml
kubectl apply -f manifests-observabilite/alertmanager-deployment.yaml
kubectl apply -f manifests-observabilite/alertmanager-service.yaml
kubectl apply -f manifests-observabilite/grafana-datasource.yaml
kubectl apply -f manifests-observabilite/grafana-dashboard-provider.yaml
kubectl apply -f manifests-observabilite/grafana-dashboard-configmap.yaml
kubectl apply -f manifests-observabilite/grafana-deployment.yaml
kubectl apply -f manifests-observabilite/grafana-service.yaml
kubectl apply -f manifests-observabilite/grafana-ingress.yaml

echo "Stack de supervision déployée."
