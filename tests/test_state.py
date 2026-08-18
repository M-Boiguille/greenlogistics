"""Tests du module core/state."""

from pathlib import Path
from tempfile import TemporaryDirectory

from core.state import Player, Progress, load_career, load_progress, save_progress


def test_load_and_save_progress():
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "progress.yml"
        progress = Progress(
            player=Player(
                name="autodidact",
                current_level="junior",
                current_mission="greenlogistics",
                certifications=[{"name": "LFCS", "status": "obtained"}],
                active_courses=[],
            ),
            skills={"Docker": 75, "Kubernetes": 55},
            known_concepts=["pods"],
            upcoming_concepts=["ingress"],
            completed_missions=["greenlogistics-001"],
        )
        save_progress(progress, path)
        loaded = load_progress(path)
        assert loaded.player.name == "autodidact"
        assert loaded.player.current_level == "junior"
        assert loaded.skills["Docker"] == 75
        assert loaded.completed_missions == ["greenlogistics-001"]


def test_load_career_default():
    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "career.yml"
        career = load_career(path)
        assert career["level"] == "junior"
        assert career["xp"] == 0
        assert career["missions_completed"] == []
