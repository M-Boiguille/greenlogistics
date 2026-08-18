# Cahier des charges — Plateforme d'hébergement

*Document fictif — scénario portfolio*

**Phase 4** — Mise en place plateforme (3 semaines) | MB Data × GreenLogistics

## Contexte (AI_STORY)

- **Intervenants** : SRE, administrateur système MB Data — GreenLogistics non impliqué (service opéré)
- **Objectif** : cluster opérationnel, observabilité de base, sauvegardes, tests de charge préliminaires

## Périmètre lab OCI (ce que tu implémentes)

| Composant | À réaliser |
|-----------|------------|
| Provisionnement | Terraform provider OCI — VM Ampere, VCN, security lists |
| Configuration | Ansible — Debian durci, k3s, WireGuard |
| Stockage / ingress | Traefik, local-path, cert-manager |
| Sauvegardes | pg_dump planifié (préparation BDD apps) |
| Tests | Validation dimensionnement [specs](../03-conception-architecture/specs.md) |

## Périmètre cible client Lyon (documentation seule)

| Composant | Référence DAT partie A |
|-----------|----------------------|
| Hyperviseur | Proxmox / Terraform libvirt |
| Cluster | kubeadm 3 nœuds |
| Observabilité | Prometheus, Grafana, OTel |
| Identité | Keycloak |
| Sauvegardes | pg_dump + Velero |

## Livrables documentaires (à compléter après implémentation)

- [Synthèse environnement](synthese-environnement.md) — URLs, IP, namespaces
- [Rapport tests performance](rapport-tests-performance.md) — résultats charge préliminaire
- Runbook personnel d'exploitation (hors repo ou local)

## Livrables techniques (à coder par l'ingénieur DevOps)

- Module Terraform OCI (VM, réseau, disque)
- Playbooks Ansible (rôles common, k3s, wireguard)
- Documentation procédure apply/destroy dans ton runbook

## Critères d'acceptation (Go)

- [ ] `terraform apply` crée la VM sans erreur
- [ ] k3s node `Ready`, Traefik accessible
- [ ] WireGuard : accès admin kubectl sans SSH public
- [ ] Ressources OCI dans les limites specs (~3 OCPU, ~18 Go RAM)
- [ ] Synthèse environnement et rapport perf renseignés

## Références

- [DAT](../03-conception-architecture/DAT.md) parties A et B
- [Feuille de route](../02-audit/feuille-de-route.md) — M1–M2
- [Runbook déploiement](synthese-environnement.md)
