#!/usr/bin/env python3
"""Rendere deutsche Erklärvideos aus Standbildern und Sprachaufnahmen.

Benötigt Python 3 sowie ffmpeg und ffprobe im PATH. Keine Python-Pakete nötig.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def format_srt_time(seconds: float) -> str:
    """Gibt Sekunden als SRT-Zeitstempel aus; Rundungsüberläufe werden getragen."""
    millis = max(0, round(seconds * 1000))
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    whole_seconds, millis = divmod(millis, 1000)
    return f"{hours:02}:{minutes:02}:{whole_seconds:02},{millis:03}"


def validate_project(project: Any) -> list[dict[str, str]]:
    if not isinstance(project, dict) or project.get("language") != "de":
        raise ValueError("Das Projekt muss language: 'de' enthalten.")
    scenes = project.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        raise ValueError("Das Projekt muss mindestens eine Szene enthalten.")
    for number, scene in enumerate(scenes, start=1):
        if not isinstance(scene, dict):
            raise ValueError(f"Szene {number} muss ein Objekt sein.")
        for key in ("image", "audio", "subtitle"):
            if not isinstance(scene.get(key), str) or not scene[key].strip():
                raise ValueError(f"Szene {number}: '{key}' muss ein nichtleerer Text sein.")
    return scenes


def run(command: list[str]) -> str:
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"Befehl fehlgeschlagen ({result.returncode}): {detail}")
    return result.stdout.strip()


def audio_duration(audio: Path) -> float:
    result = run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(audio),
    ])
    try:
        duration = float(result)
    except ValueError as exc:
        raise RuntimeError(f"Audiodauer konnte nicht ermittelt werden: {audio}") from exc
    if duration <= 0:
        raise RuntimeError(f"Audiodatei hat keine positive Dauer: {audio}")
    return duration


def srt_escape(text: str) -> str:
    return text.replace("-->", "—>").replace("\r\n", "\n").replace("\r", "\n").strip()


def render(project_path: Path, output_path: Path, fps: int = 30) -> tuple[Path, Path]:
    if fps < 1 or fps > 60:
        raise ValueError("Die Bildrate muss zwischen 1 und 60 liegen.")
    if shutil.which("ffmpeg") is None or shutil.which("ffprobe") is None:
        raise RuntimeError("ffmpeg und ffprobe müssen installiert und im PATH verfügbar sein.")

    project_path = project_path.resolve()
    base_dir = project_path.parent
    project = json.loads(project_path.read_text(encoding="utf-8"))
    scenes = validate_project(project)
    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    subtitle_path = output_path.with_suffix(".srt")
    cues: list[tuple[float, float, str]] = []

    with tempfile.TemporaryDirectory(prefix="xiaohei-video-") as temp:
        temp_dir = Path(temp)
        segment_paths: list[Path] = []
        elapsed = 0.0
        for index, scene in enumerate(scenes, start=1):
            image = (base_dir / scene["image"]).resolve()
            audio = (base_dir / scene["audio"]).resolve()
            if not image.is_file():
                raise FileNotFoundError(f"Bild für Szene {index} nicht gefunden: {image}")
            if not audio.is_file():
                raise FileNotFoundError(f"Audio für Szene {index} nicht gefunden: {audio}")
            duration = audio_duration(audio)
            cues.append((elapsed, elapsed + duration, srt_escape(scene["subtitle"])))
            elapsed += duration
            segment = temp_dir / f"scene-{index:04}.mp4"
            run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-loop", "1", "-framerate", str(fps), "-i", str(image),
                "-i", str(audio), "-map", "0:v:0", "-map", "1:a:0",
                "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,"
                      "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:white,format=yuv420p",
                "-c:v", "libx264", "-preset", "medium", "-tune", "stillimage",
                "-r", str(fps), "-c:a", "aac", "-b:a", "192k", "-shortest",
                "-movflags", "+faststart", str(segment),
            ])
            segment_paths.append(segment)

        manifest = temp_dir / "concat.txt"
        manifest.write_text(
            "".join("file '" + str(path).replace("'", "'\\''") + "'\n" for path in segment_paths),
            encoding="utf-8",
        )
        run([
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "concat",
            "-safe", "0", "-i", str(manifest), "-c", "copy", "-movflags", "+faststart",
            str(output_path),
        ])

    with subtitle_path.open("w", encoding="utf-8", newline="\n") as srt:
        for index, (start, end, text) in enumerate(cues, start=1):
            srt.write(f"{index}\n{format_srt_time(start)} --> {format_srt_time(end)}\n{text}\n\n")
    return output_path, subtitle_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Pfad zur project.json")
    parser.add_argument("--output", type=Path, default=Path("erklaervideo.mp4"), help="MP4-Zieldatei")
    parser.add_argument("--fps", type=int, default=30, help="Bildrate (Standard: 30)")
    args = parser.parse_args()
    try:
        video, subtitles = render(args.project, args.output, args.fps)
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"Fehler: {exc}", file=sys.stderr)
        return 1
    print(f"Video: {video}\nUntertitel: {subtitles}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
