#!/usr/bin/env python3
"""Repository-root launcher for the renderer bundled with the Codex skill."""

from pathlib import Path
import sys

_skill_scripts = Path(__file__).resolve().parents[1] / "xiaohei-erklaervideos" / "scripts"
sys.path.insert(0, str(_skill_scripts))
from render_video import audio_duration, format_srt_time, main, render, validate_project  # noqa: E402,F401

if __name__ == "__main__":
    raise SystemExit(main())
