"""Génération du dashboard statique."""

import json
from pathlib import Path
from typing import Any

from .state import load_career, load_progress

METRICS_FILE = Path("web/metrics.json")


def generate_metrics() -> dict[str, Any]:
    """Génère le fichier metrics.json pour le dashboard."""
    progress = load_progress()
    career = load_career()

    return {
        "player": progress.player.name,
        "level": progress.player.current_level,
        "xp": career.get("xp", 0),
        "missions_completed": len(career.get("missions_completed", [])),
        "skills": progress.skills,
        "known_concepts_count": len(progress.known_concepts),
        "upcoming_concepts_count": len(progress.upcoming_concepts),
        "active_courses": [c["name"] for c in progress.player.active_courses],
    }


def update_dashboard() -> Path:
    """Écrit le fichier metrics.json."""
    METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)
    metrics = generate_metrics()
    METRICS_FILE.write_text(json.dumps(metrics, indent=2, ensure_ascii=False), encoding="utf-8")
    return METRICS_FILE
