# SPEC — GreenLogistics DevOps RPG

## 1. Objectif

Créer un simulateur de carrière DevOps autodidacte, projet personnel et public, où l'IA génère des missions just-in-time. Le joueur progresse de Stagiaire à Lead en résolvant des missions réalistes, dans des repos séparés clonables par un recruteur.

## 2. Caractéristiques du projet

- **Projet personnel** : un seul joueur, pas de plateforme multi-utilisateurs.
- **Public** : le repo est consultable par les recruteurs.
- **Prouvable** : chaque génération d'IA est tracée (issue, prompt, réponse brute, cache).
- **Pédagogique** : les missions respectent un ratio 70% connu / 30% nouveau, tiré de `data/progress.yml`.

## 3. Stack technique

| Composant | Choix |
|-----------|-------|
| Langage | Python 3.11 |
| LLM | Deepseek par défaut, abstraction possible vers OpenAI/Claude |
| Tests | pytest |
| Linter | ruff |
| Typage | mypy (mode strict sur `core/`) |
| CI/CD | GitHub Actions |
| State | YAML (`data/progress.yml`, `data/state/career.yml`) |
| Missions | Repos GitHub séparés, clonables, ce repo hub en orchestrateur |
| Dashboard | Site statique dans `web/`, généré automatiquement |

## 4. Architecture des dossiers

```text
greenlogistics/              # Hub orchestrateur
├── .github/
│   ├── scripts/             # Scripts exécutés par les workflows
│   │   ├── generate_mission.py
│   │   ├── review_mission.py
│   │   └── update_dashboard.py
│   └── workflows/
│       ├── generate-mission.yml
│       ├── review-mission.yml
│       └── update-dashboard.yml
├── core/                    # Moteur du simulateur (testé)
│   ├── __init__.py
│   ├── llm.py               # Client LLM abstrait
│   ├── state.py             # Gestion du state joueur
│   ├── prompts.py           # Chargement et formatage des prompts
│   ├── po.py                # Génération de mission
│   ├── lead.py              # Review de mission
│   ├── evaluator.py         # Bilan de session
│   └── cache.py             # Cache des réponses LLM
├── prompts/                 # Prompts versionnés
│   ├── po.txt
│   ├── lead.txt
│   ├── mentor.txt
│   └── evaluator.txt
├── data/                    # État du joueur (partiellement gitignoré)
│   ├── progress.yml         # Niveau connu public
│   ├── state/
│   │   └── career.yml       # Missions validées, XP (public)
│   └── cache/               # Cache des réponses IA (public)
├── missions/                # Manifestes des scénarios
│   └── greenlogistics/
│       ├── manifest.yml
│       └── docs/            # Scénario narratif
├── web/                     # Dashboard statique
│   ├── index.html
│   ├── style.css
│   └── script.js
├── tests/                   # Tests unitaires
├── career.py                # CLI joueur
├── README.md
├── project_goal.md
├── SPEC.md                  # Ce fichier
├── CLAUDE.md                # Règles pour l'IA
├── TASKS.md                 # Backlog atomisé
└── AUDIT.md                 # Guide de vérification
```

## 5. Flux métier

```text
1. Merge d'une PR mission N sur le repo de mission
2. GitHub Actions du repo hub déclenche `generate-mission.yml`
3. `generate_mission.py` :
   - lit `data/progress.yml`
   - appelle Deepseek avec `prompts/po.txt`
   - sauvegarde la réponse dans `data/cache/po/{mission_id}.json`
   - crée une issue `[Mission greenlogistics-XXX] ...` dans le repo hub
4. Le joueur relit l'issue, la refuse éventuellement avec motif, ou l'accepte
5. Le joueur crée une branche `mission/greenlogistics-XXX`
6. Le joueur travaille dans le repo de mission ou dans une branche dédiée
7. `career.py --submit` ou push crée/ouvre une PR
8. `review-mission.yml` se déclenche
9. `review_mission.py` :
   - récupère les fichiers modifiés
   - appelle Deepseek avec `prompts/lead.txt`
   - poste un commentaire de review
   - approuve la PR si `decision == "APPROUVÉ"`
10. Le joueur merge
11. `update-dashboard.yml` regénère `web/index.html`
12. Retour en 1
```

## 6. Décisions majeures tranchées

| Sujet | Décision |
|-------|----------|
| Utilisateurs | Un seul (projet perso) |
| Langage | Python 3.11 |
| LLM | Deepseek par défaut, abstraction possible |
| Tests | pytest |
| Linter/typage | ruff + mypy |
| Redemander une mission | Oui, avec justification dans l'issue ou dans `data/state/rejected.yml` |
| Repos de missions | Séparés du hub, clonables par employeur |
| Fin de mission | `career.py --submit` (par défaut) ou push manuel |
| `progress.yml` | Anonymisé (`player: autodidact`) |
| `generate-mission` | Au merge d'une PR |
| `review-mission` | À l'ouverture d'une PR |
| Format des missions | Issues GitHub |
| Lead IA | Approbation automatique si OK, sinon commentaire statut via API |
| Séquence | Une mission après l'autre (pas de parallèle) |
| Dashboard | Oui, dans MVP |
| `career.py` | Oui, dans MVP |
| Gestion des échecs | Oui, refus de mission avec recadrage |
| Budget IA | 50€ max, cache activé |
| Prompts | Longs et explicites, versionnés |
| Transparence | Prompts publics, réponses brutes en issues, `AUDIT.md` |
| Sécurité | GitHub Secrets pour `DEEPSEEK_API_KEY`, token Actions suffisant |

## 7. Gestion des repos de missions

Le hub `greenlogistics/` orchestre. Les missions elles-mêmes sont réalisées dans des repos séparés, par exemple :

```text
greenlogistics-mission-001-terraform-oci/
greenlogistics-mission-002-helm-traefik/
```

Chaque repo de mission contient :
- `README.md` : contexte et objectif
- le code de la solution
- son propre historique de commits
- éventuellement un workflow de test basique

Le recruteur peut cloner et exécuter/tester directement.

## 8. Cycle d'une mission

### 8.1 Génération

- Issue créée dans `greenlogistics/`.
- Le titre contient `[Mission greenlogistics-XXX] <titre>`.
- Le body contient le contexte, les critères d'acceptation, les notions nouvelles.
- Le fichier `data/cache/po/greenlogistics-XXX.json` contient le prompt envoyé et la réponse brute.

### 8.2 Acceptation / refus

- Si le joueur refuse, il commente l'issue avec le motif.
- `data/state/rejected.yml` enregistre le refus.
- Un workflow `regenerate-mission.yml` peut être déclenché manuellement.

### 8.3 Réalisation

- Le joueur crée une branche `mission/greenlogistics-XXX`.
- Le joueur code dans le repo de mission ou dans une branche de test du hub.
- `career.py --submit` crée/ouvre la PR.

### 8.4 Review

- Le Lead IA commente la PR.
- Si `APPROUVÉ`, le workflow approuve la PR.
- Sinon, le joueur corrige et repousse.

### 8.5 Validation

- Merge de la PR.
- `data/state/career.yml` est mis à jour (XP, missions validées).
- `data/progress.yml` est mis à jour si de nouvelles compétences sont validées.
- Dashboard regénéré.
- Nouvelle mission générée.

## 9. Format des missions générées

```json
{
  "mission_id": "greenlogistics-001",
  "title": "...",
  "level": "junior",
  "description": "...",
  "new_concepts": ["cert-manager", "ingress"],
  "prerequisites": ["k3s", "services"],
  "acceptance_criteria": ["...", "..."],
  "estimated_time_minutes": 180,
  "deliverables": ["README.md", "helm/values.yaml"]
}
```

## 10. Dashboard

Le dashboard est un site statique dans `web/`.

Il affiche :
- Niveau actuel
- Nombre de missions validées
- Radar des compétences
- Dernières missions générées
- Liens vers les issues et les repos de missions
- Historique des cours KodeKloud

Les données sont dans `data/dashboard/metrics.json`, généré par `core/dashboard.py`.

## 11. Cache LLM

Pour respecter le budget 50€, chaque appel LLM est caché.

- Clé de cache : hash du prompt + modèle.
- Stockage : `data/cache/{role}/{hash}.json`.
- TTL : 30 jours par défaut.
- Réutilisation automatique si le prompt est identique.

## 12. Tests

- `tests/test_state.py` : chargement/sauvegarde du state
- `tests/test_llm.py` : mock du client LLM
- `tests/test_po.py` : génération de mission structurée
- `tests/test_cache.py` : cache hit / miss
- Tests exécutés via GitHub Actions sur chaque PR

## 13. Règles non négociables

1. Aucune logique métier dans `career.py` ou dans `.github/scripts/` — uniquement des orchestrateurs.
2. Tous les prompts sont dans `prompts/`.
3. Tous les appels LLM passent par `core/llm.py`.
4. Chaque tâche de code est testée avant commit.
5. Aucun `Any` dans `core/` sans justification écrite.
6. Pas de secret dans le repo — GitHub Actions Secrets obligatoire.

## 14. Preuve et transparence

Voir `AUDIT.md`.
