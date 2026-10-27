# Xiaohei – deutsche Erklärvideos

> Aus komplexen Gedanken werden verständliche, deutschsprachige Erklärvideos – mit ruhigen Erzähltexten, skurrilen handgezeichneten Bildern und Xiaohei, dem ernsthaften kleinen schwarzen Arbeiter.
>
> Querformat 16:9 · deutsche Sprechertexte und Untertitel · Bildsequenzen im Xiaohei-Stil · MP4 + SRT

## Was ist dieses Projekt?

Dieses Projekt überträgt und erweitert [Ian Xiaohei Illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations), einen MIT-lizenzierten Skill zum Erzeugen von Artikelillustrationen. Die deutsche Ableitung macht daraus einen Arbeitsablauf für Erklärvideos: Ein Thema oder Text wird in ein deutsches Skript, ein Storyboard mit einzelnen Szenen, passende Bilder und Sprachaufnahmen überführt. Ein beiliegendes FFmpeg-Skript setzt Szenenbilder und Audiodateien zu einem Video mit Untertiteldatei zusammen.

Die ursprünglichen Beispielbilder sind Stilreferenzen und enthalten chinesische Beschriftungen. Sie sind nicht automatisch übersetzt und sollen nicht als fertige deutsche Szenen verwendet werden. Die Autoren- und Lizenzhinweise des Originals bleiben erhalten.

## Was es erzeugt

- ein verständliches, natürlich gesprochenes deutsches Sprecher-Skript
- ein Szenen-Storyboard mit Bildideen und kurzen deutschen Einblendungen
- einzelne 16:9-Szenenbilder im zurückhaltenden Xiaohei-Stil
- ein MP4-Video und eine separate SRT-Untertiteldatei

Für die Erzeugung neuer Bilder und Sprachaufnahmen braucht der verwendete KI-Agent passende Bild- und TTS-Funktionen. Der Renderer selbst benötigt nur Python 3, `ffmpeg` und `ffprobe`; er erzeugt keine Bilder oder Stimmen und behauptet das auch nicht.

## Voraussetzungen

- Python 3.9 oder neuer
- `ffmpeg` und `ffprobe` im `PATH`
- ein KI-Agent mit Bildgenerierung und optional Text-to-Speech, wenn Bilder und Sprecher-Audio automatisch erzeugt werden sollen

## Installation als Codex-Skill

```bash
git clone https://github.com/DannySotzny/deutsche-erklaervideos-xiaohei.git
cd deutsche-erklaervideos-xiaohei
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./xiaohei-erklaervideos "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Danach im Agenten verwenden:

```text
Nutze $xiaohei-erklaervideos und erstelle aus diesem Thema ein deutsches Erklärvideo.
```

Der Skill funktioniert als Arbeitsanweisung auch mit anderen Agenten; die Aktivierung und Bild-/Audiowerkzeuge hängen vom jeweiligen Agenten ab.

## Video rendern

Lege pro Szene ein Standbild, eine Sprachaufnahme und einen kurzen deutschen Untertitel an. Pfade in der JSON-Datei sind relativ zu dieser Datei. Ein vollständiges Schema steht in [`examples/video-project.example.json`](examples/video-project.example.json).

```bash
python3 scripts/render_video.py examples/video-project.example.json --output ausgabe/erklaervideo.mp4
```

Wenn du nur den Skill installiert hast, rufe stattdessen `scripts/render_video.py` aus dem installierten Ordner `xiaohei-erklaervideos` auf. Der Renderer erstellt außerdem `ausgabe/erklaervideo.srt`. Für jede Szene wird die Länge der Audiodatei ausgelesen. Das Bild wird auf 1920×1080 eingepasst; das Seitenverhältnis bleibt erhalten, freie Flächen werden weiß aufgefüllt. Die SRT-Datei lässt sich in Videoplayern und Plattformen als Untertitelspur laden.

## Arbeitsablauf

1. Thema, Zielgruppe und Lernziel klären; bei fehlenden Angaben sinnvolle Vorschläge kenntlich machen.
2. Eine präzise Kernaussage und einen roten Faden bestimmen.
3. Einen natürlichen deutschen Sprechertext in kurze Szenen gliedern.
4. Zu jeder Szene ein eigenständiges visuelles Motiv und eine kurze Einblendung entwerfen.
5. Bilder und, sofern verfügbar, deutsche Sprachaufnahmen erzeugen.
6. Inhalt, Aussprache, Lesbarkeit und Szenenfolge prüfen.
7. Ein Projekt-JSON schreiben und MP4 sowie SRT mit dem Renderer erstellen.
8. Ausgabedateien und etwaige fehlende Komponenten ehrlich benennen.

## Stil und Qualitätsregeln

- Weißer Hintergrund, schwarze handgezeichnete Linien, viel freie Fläche.
- Wenige Akzente in Rot, Orange und Blau; kein überladener Folien- oder Infografik-Look.
- Xiaohei (小黑) handelt in der Szene mit, statt als Dekoration herumzustehen.
- Jede Szene vermittelt nur eine zentrale Aussage.
- Das gesprochene Deutsch soll natürlich, klar und auf die Zielgruppe abgestimmt sein.
- Kurze, gut lesbare deutsche Beschriftungen; keine langen Textblöcke in Bildern.
- Keine ungeprüften Fakten, erfundenen Quellen, fremden Stimmen oder nicht lizenzierten Musikstücke.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Projektstruktur

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── scripts/render_video.py          # Aufruf aus dem Repository-Stamm
├── tests/test_render_video.py
├── examples/video-project.example.json
├── examples/prompts.md
└── xiaohei-erklaervideos/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── scripts/render_video.py      # eigenständig installierbarer Renderer
    ├── templates/video-project.example.json
    ├── assets/examples/             # unveränderte Stilreferenzen aus dem Original
    └── references/
```

## Herkunft und Lizenz

Deutsche Übersetzung und Video-Workflow auf Grundlage von Ian Xiaohei Illustrations von Ian. Der ursprüngliche MIT-Lizenztext und die Hinweise zur Namensnennung liegen bei. Siehe [`NOTICE.md`](NOTICE.md) und [`LICENSE`](LICENSE).
