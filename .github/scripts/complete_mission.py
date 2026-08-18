#!/usr/bin/env python3
"""Marque une mission comme terminée et déclenche la génération de la suivante."""

import os
import re
import subprocess
import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from core.state import load_career, load_progress, save_career, save_progress

REPO = os.environ.get("GITHUB_REPOSITORY", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
PR_NUMBER = os.environ.get("PR_NUMBER", "")


def get_pr_info():
    if not REPO or not GITHUB_TOKEN or not PR_NUMBER:
        raise ValueError("GITHUB_REPOSITORY, GITHUB_TOKEN ou PR_NUMBER manquant")
    url = f"https://api.github.com/repos/{REPO}/pulls/{PR_NUMBER}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def extract_mission_id(title):
    match = re.search(r"\[Mission (greenlogistics-\d{3})\]", title)
    if not match:
        raise ValueError(f"Titre de PR invalide : {title}")
    return match.group(1)


def update_career(mission_id, level="junior"):
    career = load_career()
    completed = set(career.get("missions_completed", []))
    completed.add(mission_id)
    career["missions_completed"] = sorted(completed)
    career["xp"] = career.get("xp", 0) + 100
    career["level"] = level
    save_career(career)
    return career


def update_progress(mission_id):
    progress = load_progress()
    completed = set(progress.completed_missions)
    completed.add(mission_id)
    progress.completed_missions = sorted(completed)
    save_progress(progress)
    return progress


def git_commit_and_push(files, message):
    for f in files:
        subprocess.run(["git", "add", f], check=True)
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(
        ["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"],
        check=True,
    )
    subprocess.run(["git", "commit", "-m", message], check=True)
    subprocess.run(["git", "push"], check=True)


def run_generate_mission():
    subprocess.run(
        [sys.executable, ".github/scripts/generate_mission.py"],
        cwd=Path(__file__).parent.parent.parent,
        check=True,
    )


def main():
    pr = get_pr_info()
    if not pr.get("merged"):
        print("PR non mergée. Rien à faire.")
        return

    mission_id = extract_mission_id(pr["title"])
    print(f"Mission complétée : {mission_id}")

    update_career(mission_id)
    update_progress(mission_id)

    git_commit_and_push(
        ["data/state/career.yml", "data/progress.yml"],
        f"chore: complete mission {mission_id}",
    )
    print("State mis à jour et poussé.")

    run_generate_mission()
    print("Génération de la prochaine mission déclenchée.")


if __name__ == "__main__":
    main()
