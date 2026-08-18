# Project Goal — GreenLogistics : simulateur de missions DevOps autodidacte

## Vision

Créer un système où une **IA génère mes prochaines missions DevOps just-in-time**, en s'appuyant sur mon vrai niveau (KodeKloud, LFCS, Docker). Cela prouve aux recruteurs que je maîtrise non seulement la technique, mais le **workflow d'entreprise** : tickets, reviews, merge, run, progression.

## Bases de connaissances

- **LFCS** : validé — Linux, réseau, systemd, scripting.
- **Docker** : bon niveau — images, compose, réseaux, volumes.
- **KodeKloud CKA** : en cours — core concepts, scheduling, logging/monitoring, application lifecycle, etc.
- **Autres cours KodeKloud** : suivis régulièrement et mis à jour dans `data/progress.yml`.

L'IA a accès à ce fichier pour choisir ce que je dois travailler ensuite.

## Workflow global

```text
1. Je mets à jour data/progress.yml (compétences, cours suivis, chapitres à venir)
2. Je merge une mission (PR validée par Lead IA)
3. GitHub Actions déclenche .github/workflows/generate-mission.yml
4. Le script .github/scripts/generate_mission.py lit data/progress.yml
5. Il appelle l'API Deepseek avec prompts/po.txt
6. Une issue GitHub est créée : mission #N
7. Je la relis et l'accepte (ou je la refuse avec motif)
8. Je travaille la mission, je pousse, je fais une PR
9. Le Lead IA review via prompts/lead.txt
10. Si validé, merge → retour en 2.
```

## Règles de génération des missions

Chaque mission doit respecter le ratio **70% connu / 30% nouveau** :

- 70% de compétences déjà validées (rappel, consolidation, mise en situation).
- 30% de notions à peine abordées dans mes cours KodeKloud (zone proximale).
- Parfois, un exercice de **rappel** sur Docker ou Linux.
- Parfois, un chapitre à peine terminé de KodeKloud à mettre en pratique.
- Maximum 2 nouvelles notions par mission.
- Contexte fixe : GreenLogistics, cloud privé souverain, lab OCI.

## Rôles IA

| Rôle | Fichier | Fonction |
|------|---------|----------|
| Product Owner | `prompts/po.txt` | Génère la mission sous forme d'issue |
| Lead DevOps | `prompts/lead.txt` | Review le code de la PR |
| Mentor | `prompts/mentor.txt` | Bilan pédagogique périodique |
| Evaluator | `prompts/evaluator.txt` | Met à jour le radar de compétences |

## Ce que le recruteur voit

- Des **issues générées par un workflow automatique**.
- Des **PRs avec reviews du Lead IA**.
- Un **historique de commits** montrant le travail réel.
- Un `data/progress.yml` mis à jour avec mon suivi KodeKloud.
- Des **prompts explicites** qui prouvent que je sais cadrer l'IA.

## Phases

| Phase | Objectif |
|-------|----------|
| 1 | Mission GreenLogistics générée automatiquement |
| 2 | Review automatique du Lead IA |
| 3 | Suivi des cours KodeKloud alimentant `progress.yml` |
| 4 | Génération de missions plus complexes (rappel + nouveauté) |
| 5 | Ajout d'autres missions (Vaultwarden, Memos, Vikunja) |

## Hors scope

- Journal de bord public / site web.
- Dashboard avec radar.
- Ces éléments seront traités plus tard.
