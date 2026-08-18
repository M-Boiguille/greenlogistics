# GreenLogistics — Simulateur de carrière DevOps autodidacte

> **Ne montre pas ce que tu sais. Montre comment tu apprends.**

GreenLogistics est un simulateur de missions DevOps qui me fait progresser de **Stagiaire à Lead** en reproduisant le workflow d'une vraie entreprise. Les missions sont générées **just-in-time** par une IA selon mon niveau réel, mes cours KodeKloud et mes certifications.

---

## Le principe

1. Je suis un ingénieur DevOps junior fictif chez **MB Data**.
2. Un workflow **GitHub Actions** génère une mission (issue) via l'API **Deepseek**.
3. Je code la solution dans ce repo.
4. Un **Lead IA** fait la review.
5. Si c'est validé, une nouvelle mission est générée.
6. Tout est versionné, auditable et public.

---

## Ma base de connaissances

| Source | Niveau |
|--------|--------|
| Linux Foundation Certified System Administrator (LFCS) | Validé |
| Docker | Bon niveau |
| KodeKloud — CKA | En cours (Scheduling, Application Lifecycle Management) |
| KodeKloud — DevOps/Autres | Suivi exhaustif en cours |

Le simulateur se base sur `data/progress.yml` pour connaître mes compétences exactes.

---

## Structure

```text
greenlogistics/
├── .github/
│   ├── scripts/
│   │   └── generate_mission.py   # Génère la prochaine mission
│   └── workflows/
│       └── generate-mission.yml  # Déclenche la génération
├── data/
│   └── progress.yml              # Mon vrai niveau (cours, compétences)
├── prompts/
│   ├── po.txt                    # Génère les missions
│   ├── lead.txt                  # Review du code
│   ├── mentor.txt                # Bilan pédagogique
│   └── evaluator.txt             # Évalue la session
├── missions/
│   └── greenlogistics/
│       ├── manifest.yml          # Métadonnées de la mission
│       └── docs/                 # Scénario de la mission
├── web/                          # Dashboard public (hors MVP)
└── README.md                     # Ce fichier
```

---

## Ce que montre ce repo aux recruteurs

- Je maîtrise le **workflow d'entreprise** : tickets, reviews, merge.
- Je sais **automatiser un processus** avec GitHub Actions.
- Je sais **cadrer une IA** avec des prompts, des schémas JSON.
- J'apprends en continu avec des **missions adaptées**.
- Mon évolution est **traçable publiquement**.

---

## Pour commencer

1. Lire `project_goal.md` pour la vision détaillée.
2. Consulter `data/progress.yml` pour mon niveau.
3. Lire `missions/greenlogistics/manifest.yml` pour le contexte.
4. Voir les dernières **issues générées** pour les missions en cours.

---

## Missions

- `missions/greenlogistics` : cloud privé souverain, lab OCI, CI/CD, MEP, RUN.
- D'autres missions suivront : Vaultwarden, Memos, Vikunja, Moemi.
