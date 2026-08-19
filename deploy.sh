#!/bin/bash
set -e

echo "Création du namespace..."
kubectl apply -f manifests/namespace.yaml

echo "Création du PVC, configmaps et secret..."
kubectl apply -f manifests/prometheus-pvc.yaml
kubectl apply -f manifests/prometheus-config.yaml
kubectl apply -f manifests/prometheus-alerts.yaml
kubectl apply -f manifests/grafana-secret.yaml

# Décommenter et exécuter si le secret n'est pas créé manuellement :
# kubectl create secret generic grafana-admin -n monitoring --from-literal=password='VOTRE_MOT_DE_PASSE'

echo "Création du ClusterIssuer..."
kubectl apply -f manifests/cluster-issuer.yaml

echo "Déploiement RBAC et exporters..."
kubectl apply -f manifests/kube-state-metrics-rbac.yaml
kubectl apply -f manifests/kube-state-metrics-deployment.yaml
kubectl apply -f manifests/kube-state-metrics-service.yaml
kubectl apply -f manifests/node-exporter-ds.yaml
kubectl apply -f manifests/node-exporter-service.yaml

echo "Déploiement Prometheus, Grafana et Alertmanager..."
kubectl apply -f manifests/prometheus-deployment.yaml
kubectl apply -f manifests/prometheus-service.yaml
kubectl apply -f manifests/alertmanager-deployment.yaml
kubectl apply -f manifests/alertmanager-service.yaml
kubectl apply -f manifests/grafana-datasource.yaml
kubectl apply -f manifests/grafana-dashboard-provider.yaml
kubectl apply -f manifests/grafana-dashboard-configmap.yaml
kubectl apply -f manifests/grafana-deployment.yaml
kubectl apply -f manifests/grafana-service.yaml
kubectl apply -f manifests/grafana-ingress.yaml

echo "Stack de supervision déployée."
