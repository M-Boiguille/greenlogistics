- name: CKA
  level: 1.1
  modules:
    - name: Introduction
      concepts: [kubernetes-overview, certification-format]
      completed: true
    - name: Core Concepts
      concepts: [pods, replicasets, deployments, namespaces, services, kubectl]
      completed: true
    - name: Scheduling
      concepts: [manual-scheduling, taints-tolerations, node-affinity, daemonsets, static-pods]
      completed: true
    - name: Logging and Monitoring
      concepts: [metrics-server, application-logs]
      completed: true
    - name: Application Lifecycle Management
      concepts: [rolling-updates, rollback, configmaps, secrets, init-containers, multi-container-pods]
      completed: true
    - name: Cluster Maintenance
      concepts: [os-upgrades, cluster-upgrade, etcd-backup-restore]
      completed: false
    - name: Security
      concepts: [authentication, tls-certificates, kubeconfig, rbac, cluster-roles, image-security, security-context, network-policies]
      completed: false
    - name: Storage
      concepts: [volumes, persistent-volumes, persistent-volume-claims, storage-class, csi]
      completed: false
    - name: Networking
      concepts: [cni, pod-networking, service-networking, coredns, ingress]
      completed: false
    - name: Design and Install Kubernetes Cluster
      concepts: [cluster-design, high-availability, etcd-ha]
      completed: false
    - name: Install Kubernetes the kubeadm way
      concepts: [kubeadm, cluster-provisioning]
      completed: false
    - name: Troubleshooting
      concepts: [application-failure, control-plane-failure, worker-node-failure, network-troubleshooting]
      completed: false
    - name: Other Topics
      concepts: [json-path, advanced-kubectl]
      completed: false
    - name: Mock Exams
      concepts: [exam-simulation, timed-practice]
      completed: false

- name: Kubernetes Networking
  level: 1.2
  modules:
    - name: Fondamentaux réseau (prérequis)
      concepts: [switching, routing, dns, network-namespaces]
      completed: false
    - name: CNI en profondeur
      concepts: [cni, weave, calico, cilium]
      completed: false
    - name: Service networking et Ingress
      concepts: [cluster-ip, nodeport, ingress-controllers]
      completed: false
    - name: DNS et CoreDNS
      concepts: [coredns, service-discovery]
      completed: false

- name: Git
  modules:
    - name: Bases de Git
      concepts: [git-init, commit, staging-area]
      completed: false
    - name: Branches et fusion
      concepts: [branching, merge, rebase, conflicts]
      completed: false
    - name: Dépôts distants
      concepts: [github, push, pull, clone, fork]
      completed: false
    - name: Workflows collaboratifs
      concepts: [pull-requests, git-flow, code-review]
      completed: false

- name: Shell Scripts for Beginners
  source: https://learn.kodekloud.com/courses/shell-scripts-for-beginners
  modules:
    - name: Bases du scripting shell
      concepts: [bash, shebang, variables]
      completed: false
    - name: Structures de contrôle
      concepts: [loops, conditionals, case-statements]
      completed: false
    - name: Fonctions et arguments
      concepts: [functions, positional-parameters]
      completed: false

- name: Advanced Bash Scripting
  source: https://learn.kodekloud.com/courses/advanced-bash-scripting
  modules:
    - name: Techniques bash avancées
      concepts: [arrays, subshells, process-substitution]
      completed: false
    - name: Traitement de texte
      concepts: [grep, sed, awk, regex]
      completed: false
    - name: Gestion d'erreurs
      concepts: [exit-codes, trap, set-e]
      completed: false
    - name: Scripts d'automatisation
      concepts: [cron, automation-patterns]
      completed: false

- name: Terraform Associate Certification (HashiCorp)
  source: https://learn.kodekloud.com/courses/terraform-associate-certification-hashicorp-certified
  modules:
    - name: Fondamentaux IaC
      concepts: [infrastructure-as-code, hcl, providers]
      completed: false
    - name: Workflow Terraform
      concepts: [terraform-init, plan, apply, destroy]
      completed: false
    - name: Gestion du state
      concepts: [state-file, remote-backend, state-locking]
      completed: false
    - name: Modules et provisioners
      concepts: [modules, variables, outputs, provisioners]
      completed: false
    - name: HCP Terraform / Terraform Cloud
      concepts: [terraform-cloud, workspaces, remote-execution]
      completed: false

- name: GitHub Actions
  source: https://learn.kodekloud.com/courses/github-actions
  modules:
    - name: Bases des workflows
      concepts: [yaml-workflow, jobs, steps]
      completed: false
    - name: Triggers et événements
      concepts: [on-push, on-pull-request, schedule]
      completed: false
    - name: Secrets et environnements
      concepts: [secrets, environments, permissions]
      completed: false
    - name: Workflows réutilisables
      concepts: [reusable-workflows, composite-actions, marketplace]
      completed: false

- name: AWS Cloud Practitioner (CLF-C02)
  source: https://learn.kodekloud.com/courses/aws-cloud-practitioner-clf-c02
  modules:
    - name: Concepts Cloud
      concepts: [cloud-computing, aws-global-infrastructure]
      completed: false
    - name: Sécurité et conformité
      concepts: [iam, shared-responsibility-model, compliance]
      completed: false
    - name: Technologie - services core
      concepts: [ec2, s3, vpc, rds, lambda]
      completed: false
    - name: Facturation et pricing
      concepts: [billing, pricing-models, support-plans]
      completed: false

- name: Ansible Basics
  source: https://learn.kodekloud.com/courses/learn-ansible-basics-beginners-course
  modules:
    - name: Fondamentaux Ansible
      concepts: [agentless, ssh, idempotency]
      completed: false
    - name: Inventaire et playbooks
      concepts: [inventory, playbooks, yaml]
      completed: false
    - name: Commandes ad-hoc
      concepts: [ad-hoc-commands, modules]
      completed: false
    - name: Roles et templates
      concepts: [roles, jinja2-templates, variables]
      completed: false

- name: Fundamentals of DevOps
  source: https://learn.kodekloud.com/courses/fundamentals-of-devops
  modules:
    - name: Culture DevOps
      concepts: [calms-framework, collaboration, devops-culture]
      completed: false
    - name: CI/CD fondamentaux
      concepts: [continuous-integration, continuous-delivery]
      completed: false
    - name: Infrastructure as Code
      concepts: [iac-principles, configuration-management]
      completed: false
    - name: Monitoring et feedback loops
      concepts: [observability, feedback-loops]
      completed: false

- name: Crash Course - AI-Powered DevOps
  source: https://learn.kodekloud.com/courses/crash-course-ai-powered-devops
  modules:
    - name: Bases LLM et MCP
      concepts: [llm-basics, mcp, ai-agents]
      completed: false
    - name: Agents IA pour l'infra
      concepts: [docker-optimizer-agent, terraform-security-agent]
      completed: false
    - name: CI/CD assisté par IA
      concepts: [ai-powered-pipelines, automation]
      completed: false
    - name: Réponse aux incidents avec des agents IA
      concepts: [ai-incident-commander, kubernetes-troubleshooting-ai]
      completed: false

- name: Introduction to k8sgpt and AI-driven Kubernetes Engineering
  source: https://learn.kodekloud.com/courses/introduction-to-k8sgpt-and-ai-driven-kubernetes-engineering
  modules:
    - name: Introduction à k8sgpt
      concepts: [k8sgpt, cluster-analysis]
      completed: false
    - name: Diagnostic de cluster assisté par IA
      concepts: [ai-diagnostics, root-cause-analysis]
      completed: false
    - name: Intégration LLM et Kubernetes
      concepts: [llm-integration, kubectl-ai]
      completed: false
    - name: Remédiation automatisée
      concepts: [automated-remediation]
      completed: false

- name: Claude Code for Beginners
  source: https://learn.kodekloud.com/courses/claude-code-for-beginners
  modules:
    - name: Installation et configuration
      concepts: [claude-code-setup, cli-basics]
      completed: false
    - name: Workflows de codage agentique
      concepts: [agentic-coding, task-delegation]
      completed: false
    - name: Intégration MCP
      concepts: [mcp-servers, tool-use]
      completed: false
    - name: Automatisation des tâches dev
      concepts: [code-review-automation, refactoring]
      completed: false

- name: GitHub Copilot in Action
  source: https://learn.kodekloud.com/courses/github-copilot-in-action
  modules:
    - name: Fondamentaux Copilot
      concepts: [code-completion, suggestions]
      completed: false
    - name: Copilot Chat
      concepts: [copilot-chat, prompt-patterns]
      completed: false
    - name: Copilot pour les tâches DevOps
      concepts: [ci-cd-assistance, yaml-generation]
      completed: false
    - name: Bonnes pratiques
      concepts: [ai-assisted-review, prompt-engineering]
      completed: false

- name: Prometheus Certified Associate (PCA)
  source: https://learn.kodekloud.com/courses/prometheus-certified-associate-pca
  modules:
    - name: Architecture Prometheus
      concepts: [prometheus-architecture, time-series-db]
      completed: false
    - name: PromQL
      concepts: [promql, queries, aggregations]
      completed: false
    - name: Alerting
      concepts: [alertmanager, alert-rules]
      completed: false
    - name: Exporters et service discovery
      concepts: [exporters, service-discovery]
      completed: false

- name: Grafana Loki
  source: https://learn.kodekloud.com/courses/grafana-loki
  modules:
    - name: Architecture Loki
      concepts: [loki-architecture, log-aggregation]
      completed: false
    - name: LogQL
      concepts: [logql, queries]
      completed: false
    - name: Pipelines d'agrégation de logs
      concepts: [promtail, log-pipelines]
      completed: false
    - name: Dashboards Grafana pour les logs
      concepts: [grafana-dashboards]
      completed: false

- name: EFK Stack - Enterprise Grade Logging and Monitoring
  source: https://learn.kodekloud.com/courses/efk-stack-enterprise-grade-logging-and-monitoring
  modules:
    - name: Fondamentaux Elasticsearch
      concepts: [elasticsearch, indexing]
      completed: false
    - name: Fluentd / Fluent Bit
      concepts: [fluentd, fluent-bit, log-collection]
      completed: false
    - name: Dashboards Kibana
      concepts: [kibana, visualization]
      completed: false
    - name: Pipeline de logging Kubernetes
      concepts: [kubernetes-logging, daemonset-logging]
      completed: false

- name: AWS Solutions Architect Associate
  source: https://learn.kodekloud.com/courses/aws-solutions-architect-associate-certification
  modules:
    - name: Architectures résilientes
      concepts: [high-availability, disaster-recovery]
      completed: false
    - name: Architectures performantes
      concepts: [elasticity, caching, performance]
      completed: false
    - name: Architectures sécurisées
      concepts: [iam, encryption, vpc-security]
      completed: false
    - name: Optimisation des coûts
      concepts: [cost-optimization, reserved-instances]
      completed: false

- name: Certified Kubernetes Security Specialist (CKS)
  source: https://learn.kodekloud.com/courses/certified-kubernetes-security-specialist-cks
  modules:
    - name: Durcissement du cluster
      concepts: [cluster-hardening, cis-benchmark]
      completed: false
    - name: Durcissement système
      concepts: [system-hardening, apparmor, seccomp]
      completed: false
    - name: Réduction des vulnérabilités microservices
      concepts: [pod-security-standards, network-policies]
      completed: false
    - name: Sécurité de la supply chain
      concepts: [image-scanning, admission-controllers, supply-chain-security]
      completed: false
    - name: Monitoring et sécurité runtime
      concepts: [falco, runtime-security, audit-logging]
      completed: false

- name: AIOps Foundations
  source: https://learn.kodekloud.com/courses/aiops-foundations-intelligent-monitoring-with-prometheus-grafana
  modules:
    - name: Concepts de monitoring intelligent
      concepts: [aiops-concepts, intelligent-monitoring]
      completed: false
    - name: Prometheus et Grafana pour l'AIOps
      concepts: [prometheus, grafana]
      completed: false
    - name: Bases de la détection d'anomalies
      concepts: [anomaly-detection-basics]
      completed: false
    - name: Corrélation d'alertes
      concepts: [alert-correlation]
      completed: false

- name: AIOps in Practice - Logging, Alerting at Scale
  source: https://learn.kodekloud.com/courses/aiops-in-practice-logging-alerting-at-scale
  modules:
    - name: Logging centralisé à grande échelle
      concepts: [centralized-logging, scale]
      completed: false
    - name: Stratégies d'alerting
      concepts: [alerting-strategies]
      completed: false
    - name: Réduction du bruit
      concepts: [noise-reduction, alert-deduplication]
      completed: false
    - name: Corrélation d'incidents
      concepts: [incident-correlation]
      completed: false

- name: Chaos Engineering
  source: https://learn.kodekloud.com/courses/chaos-engineering
  modules:
    - name: Principes du chaos engineering
      concepts: [chaos-engineering-principles, resilience]
      completed: false
    - name: Conception d'expériences
      concepts: [experiment-design, hypothesis-testing]
      completed: false
    - name: Outils (Litmus, Chaos Mesh)
      concepts: [litmus, chaos-mesh]
      completed: false
    - name: Game days et tests de résilience
      concepts: [game-days, resilience-testing]
      completed: false

- name: DevOps Interview Preparation Course
  source: https://learn.kodekloud.com/courses/devops-interview-preparation-course
  modules:
    - name: Sujets techniques d'entretien
      concepts: [technical-questions, tooling-review]
      completed: false
    - name: System design pour DevOps
      concepts: [system-design, architecture-questions]
      completed: false
    - name: Questions comportementales
      concepts: [behavioral-questions, star-method]
      completed: false
    - name: Entretiens blancs
      concepts: [mock-interviews]
      completed: false
