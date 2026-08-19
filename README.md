# GreenLogistics — Simulateur SRE / DevOps confirmé

> **Je ne simule pas un junior. Je m'entraîne à tenir la production.**

**Rôle visé :** Ingénieur SRE / DevOps confirmé, profil technique en reconversion.  
**Cible :** Poste en fiabilisation, sécurisation et industrialisation d'infrastructures Kubernetes.

Ce repo est mon **environnement de travail simulé**. Un moteur IA me génère des missions techniques just-in-time, un Lead IA fait la review de mes PRs, et je livre des solutions orientées **production** : déploiement, incident, hardening, observabilité, reprise d'activité, documentation ops.

---

## Pourquoi ce repo est différent

La plupart des juniors montrent des certificats et des tutos. Moi, je montre **un workflow d'exploitation** :

- Des **missions non prévues** générées par IA selon mon niveau confirmé.
- Des **PRs** avec review automatique par un Lead IA.
- Un **processus de merge** déclenchant la mission suivante.
- Un **dashboard public** de progression.
- Des **runbooks, post-mortems et DAT** dans les livrables.
- Une **preuve d'apprentissage** : chaque génération, chaque review, chaque correction est versionnée.

> Ce n'est pas un portfolio junior. C'est une preuve de méthode pour un poste de SRE.

---

## Ce que ce repo prouve

| Compétence démontrée | Preuve dans le repo |
|----------------------|---------------------|
| **Workflow d'exploitation** | Issues, PRs, reviews, merge, CI/CD |
| **Automatisation** | `.github/workflows/` génère, review, évalue, déploie |
| **Cadrage d'IA** | Prompts versionnés dans `prompts/`, JSON structuré |
| **Kubernetes en production** | Livrables `k8s/`, runbooks, tests de validité |
| **Sécurité & secrets** | GitHub Secrets, RBAC, network policies, cert-manager |
| **Observabilité** | Prometheus, Loki, Grafana (missions à venir) |
| **Gestion de version** | Conventional commits, tests, ruff, mypy |
| **Apprentissage adaptatif** | `data/courses.yml` basé sur KodeKloud, progression auto |

---

## Workflow du simulateur

```text
1. L'IA (PO) génère une mission inattendue dans une issue
2. Je crée une branche `mission/greenlogistics-XXX`
3. Je code la solution (K8s, CI/CD, IaC, observabilité...)
4. Le Lead IA review ma PR
5. Le Mentor IA évalue ma progression
6. Si validé, je merge
7. Le workflow met à jour la progression et génère la mission suivante
```

Chaque étape est **publique et auditable**.

---

## Mission en cours

→ Voir les [issues](https://github.com/M-Boiguille/greenlogistics/issues) : missions générées automatiquement par l'IA.

Les missions couvrent : exposition HTTPS, incidents, hardening, observabilité, GitOps, reprise d'activité.

---

## Stack & cible

| Domaine | Outil / Certif |
|---------|----------------|
| Linux | LFCS obtenu |
| Conteneurs | Docker avancé |
| Orchestration | Kubernetes — CKA en cours sur KodeKloud |
| Cloud | OCI Always Free |
| CI/CD | GitHub Actions |
| IaC | Terraform |
| Config Management | Ansible |
| Observabilité | Prometheus, Loki, Grafana |
| Sécurité | cert-manager, RBAC, network policies, Falco |
| Langage | Python 3.11 |
| Tests | pytest, ruff, mypy |

---

## Dashboard de progression

📊 [Voir mon dashboard public](https://M-Boiguille.github.io/greenlogistics/)

Le dashboard affiche :
- Mon niveau actuel et ma cible
- Le nombre de missions complétées
- Le radar de compétences
- Les cours KodeKloud en cours

---

## Ce que je cherche

**Poste visé :** Ingénieur SRE / DevOps confirmé, idéalement en cloud privé souverain, infrastructure critique ou PME/ETI en croissance.

**Ce que j'apporte :**
- Une expérience technique de terrain, de la maintenance à l'infrastructure.
- Une autonomie réelle sur Linux, Docker, Kubernetes, CI/CD.
- Une appétence pour la fiabilité, la sécurité et la documentation ops.
- Une capacité à cadrer et utiliser l'IA pour accélérer sans dépendre.
- Une posture SRE : quand ça casse, je répare, j'apprends, je documente.

**Localisation :** France, full remote ou région lyonnaise.

---

## Me contacter

- 💼 [LinkedIn](https://linkedin.com/in/ton-profil)
- 📧 [email@example.com](mailto:email@example.com)
- 🌐 [Mon site personnel](https://ton-site.com)

> **Mon CV ne dit pas que je sais faire. Ce repo le prouve.**
