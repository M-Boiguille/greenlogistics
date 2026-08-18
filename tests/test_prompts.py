"""Tests du module core/prompts."""

from pathlib import Path
from tempfile import TemporaryDirectory

from core.prompts import format_prompt


def test_format_prompt(monkeypatch):
    with TemporaryDirectory() as tmp:
        prompts_dir = Path(tmp)
        (prompts_dir / "test.txt").write_text("Hello {{NAME}} !", encoding="utf-8")
        monkeypatch.setattr("core.prompts.PROMPTS_DIR", prompts_dir)

        result = format_prompt("test", {"NAME": "DevOps"})
        assert result == "Hello DevOps !"
