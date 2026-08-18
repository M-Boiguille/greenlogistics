# AUDIT.md — Comment vérifier l'authenticité du simulateur

## Principe

Ce repo est conçu pour être **auditable par un recruteur**. Chaque action de l'IA est tracée, versionnée et reproductible.

## Ce que le recruteur peut vérifier

### 1. Les prompts utilisés

- Localisation : `prompts/po.txt`, `prompts/lead.txt`, `prompts/mentor.txt`, `prompts/evaluator.txt`
- Les prompts sont versionnés : on peut voir leur évolution dans `git log`.
- Ils ne contiennent aucun secret.

### 2. Les réponses brutes de l'IA

- Localisation : `data/cache/po/{mission_id}.json` et `data/cache/lead/{pr_number}.json`
- Chaque fichier contient :
  - La date de la requête
  - Le modèle utilisé
  - Le prompt envoyé
  - La réponse brute de l'IA
- Permet de vérifier que la mission a bien été générée par l'IA et non écrite à la main.

### 3. Les issues générées

- URL : https://github.com/{owner}/{repo}/issues?q=label:generated-by-ai
- Chaque issue a le label `generated-by-ai`.
- Chaque issue est liée à un `mission_id`.
- Le body de l'issue est généré à partir du JSON de `data/cache/po/`.

### 4. Les reviews automatiques

- URL : dans les PRs, onglet *Conversation* et *Files changed*
- Chaque review est un commentaire du compte `github-actions[bot]`.
- Le commentaire contient la décision `APPROUVÉ` ou `À_REVOIR`.
- Le statut de la PR est mis à jour automatiquement.

### 5. L'historique du joueur

- Fichier `data/state/career.yml` : missions validées, XP, niveau.
- Fichier `data/progress.yml` : compétences, cours suivis.
- Fichier `data/state/rejected.yml` : missions refusées avec motifs.

### 6. L'automatisation

- Workflows : `.github/workflows/`
- Scripts : `.github/scripts/`
- On peut lire le code source pour vérifier qu'il n'y a pas de trucage.
- Le recruteur peut forker le repo et relancer `generate-mission.yml` avec sa propre clé API.

### 7. Les repos de missions

- Chaque mission aboutit à un repo séparé.
- Le recruteur peut cloner le repo de mission et tester la solution.
- Les repos de mission sont liés dans le body de l'issue.

## Recommandations pour le joueur

1. Ne jamais éditer manuellement `data/cache/`.
2. Ne jamais éditer manuellement `data/state/career.yml`.
3. Toujours passer par `career.py` ou les workflows pour générer/modifier le state.
4. Faire des commits atomiques, un par micro-tâche.

## Limites

- L'IA peut halluciner. C'est pourquoi le joueur peut refuser une mission.
- Le cache peut contenir une réponse erronée. C'est pourquoi chaque PR est reviewée.
- Le simulateur n'est pas un remplacement de l'expérience réelle, mais une preuve de méthode.
