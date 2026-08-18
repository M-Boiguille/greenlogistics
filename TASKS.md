# TASKS.md — Backlog atomisé

## Phase 0 — Cadrage (done)

- [x] Créer `SPEC.md`
- [x] Créer `CLAUDE.md`
- [x] Créer `TASKS.md`
- [x] Créer `AUDIT.md`

## Phase 1 — Fondations (à faire)

- [ ] Créer `pyproject.toml` (dépendances : pyyaml, requests, pytest, ruff, mypy)
- [ ] Créer `core/llm.py` avec provider Deepseek abstrait
- [ ] Créer `core/state.py` pour lire/écrire YAML
- [ ] Créer `core/prompts.py` pour charger et formater les prompts
- [ ] Créer `core/cache.py` pour le cache des réponses LLM
- [ ] Tests unitaires pour `core/state.py`, `core/prompts.py`, `core/cache.py`
- [ ] Mettre à jour `data/progress.yml` avec profil anonymisé
- [ ] Mettre à jour `data/state/career.yml` (template)

## Phase 2 — Génération de missions

- [ ] Refactoriser `.github/scripts/generate_mission.py` pour utiliser `core/`
- [ ] Créer `core/po.py` (génération mission structurée)
- [ ] Vérifier le parsing JSON des réponses
- [ ] Créer `data/cache/po/.gitkeep`
- [ ] Tests pour `core/po.py`
- [ ] Lancer un test local de génération

## Phase 3 — Review automatique

- [ ] Créer `core/lead.py` (review d'une PR)
- [ ] Créer `.github/scripts/review_mission.py`
- [ ] Créer `.github/workflows/review-mission.yml`
- [ ] Tests pour `core/lead.py` avec mock LLM
- [ ] Lancer un test de review sur une PR fictive

## Phase 4 — CLI joueur

- [ ] Créer `career.py` avec :
  - `career.py --start` : affiche la mission en cours
  - `career.py --submit` : crée/ouvre la PR
  - `career.py --regenerate` : redemande une mission
  - `career.py --status` : affiche niveau, XP, missions
- [ ] Tests pour `career.py` (commandes sans effet de bord)

## Phase 5 — Dashboard web

- [ ] Créer `core/dashboard.py` (génère `web/metrics.json`)
- [ ] Créer `.github/workflows/update-dashboard.yml`
- [ ] Créer `web/index.html` + `style.css` + `script.js`
- [ ] Héberger le dashboard sur GitHub Pages

## Phase 6 — Gestion des échecs

- [ ] Créer `.github/workflows/regenerate-mission.yml`
- [ ] Créer `data/state/rejected.yml`
- [ ] Implémenter logique de refus/acceptation dans `career.py`

## Phase 7 — Polissage

- [ ] Ajouter `mypy` strict sur `core/`
- [ ] Ajouter `ruff` en CI
- [ ] Ajouter `pytest` en CI
- [ ] Documenter le lancement du MVP dans `README.md`
