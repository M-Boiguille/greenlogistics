# CLAUDE.md — Règles système pour l'IA

## Mission

Tu es un assistant de développement pour **GreenLogistics DevOps RPG**, un simulateur de carrière DevOps personnel et public. Tu exécutes des tâches atomiques définies dans `SPEC.md` et `TASKS.md`.

## Interdiction absolue

- Ne jamais concevoir et exécuter en même temps. Si une incohérence d'architecture est détectée, **s'arrêter et poser la question**.
- Ne jamais modifier de fichiers hors du périmètre de la tâche assignée.
- Ne jamais supprimer `SPEC.md`, `CLAUDE.md`, `TASKS.md`, `AUDIT.md`, `project_goal.md`, `data/progress.yml`.
- Ne jamais modifier `data/progress.yml` sans permission explicite.
- Ne jamais hardcoder de secret (clé API, token).
- Ne jamais committer sans tests verts sur `core/`.

## Conventions Python

- Python 3.11.
- Typage explicite, pas de `Any` dans `core/` sans justification.
- Toutes les fonctions de `core/` doivent avoir des type hints.
- Les scripts CLI (`career.py`, `.github/scripts/*.py`) sont de simples orchestrateurs : la logique est dans `core/`.
- Pas de logique métier dans les workflows ou les scripts GitHub.

## Architecture

- `core/llm.py` : seul point d'entrée pour les appels LLM.
- `core/state.py` : seul point d'entrée pour lire/écrire le state.
- `core/prompts.py` : chargement et formatage des prompts.
- `core/po.py`, `core/lead.py`, `core/evaluator.py`, `core/mentor.py` : un module par rôle.
- `prompts/*.txt` : prompts versionnés, jamais dans le code.

## Flux de travail imposé

1. Lire `SPEC.md` avant toute tâche.
2. Lire `TASKS.md` pour identifier la tâche atomique suivante.
3. Écrire d'abord le test, puis le code.
4. Exécuter `ruff check .` et `mypy core/ && pytest`.
5. Vérifier `git diff` avant proposition.
6. Un seul commit par micro-tâche validée.

## Validation par terminal

L'arbitre final est le terminal. Si `ruff`, `mypy` ou `pytest` échoue, corriger le code, pas le test.

## Gestion des erreurs

- Si un test échoue, analyser le message avant de modifier.
- Si l'IA dévie ou boucle, proposer un `git checkout .` et réécrire l'instruction initiale.
- Si un problème d'architecture est détecté, ne pas le corriger soi-même. Demander clarification.

## Génération de code

- Générer du code par petites itérations (< 100 lignes de diff).
- Une tâche = une action précise (ex. : "créer `core/llm.py`", pas "implémenter tout le LLM").
- Toujours fournir un contexte restreint : 2 ou 3 fichiers maximum.
