---
name: xiaohei-erklaervideos
description: Erstellt deutschsprachige Erklärvideos aus Themen, Artikeln, Notizen oder Dokumenten – mit Sprechertext, Storyboard, Xiaohei-Bildszenen und MP4/SRT-Rendering. Verwenden, wenn ein deutsches Erklärvideo, Lernvideo, Erklärclip, Storyboard oder eine deutschsprachige Visualisierung gewünscht ist.
---

# Xiaohei – deutsche Erklärvideos

## Ziel

Verwandle ein Thema, einen Artikel oder bereitgestellte Unterlagen in ein verständliches Erklärvideo auf Deutsch. Nutze den skurrilen, klaren Xiaohei-Zeichenstil als wiedererkennbare visuelle Sprache. Standardausgabe: Querformat 16:9, deutsche Sprecherfassung, Szenenbilder, MP4 und separate SRT-Untertitel.

Xiaohei (小黑) ist ein kleiner, schwarzer, ernsthafter Fantasiearbeiter mit weißen Punktaugen und dünnen Beinen. Er muss in den Szenen die erklärende Handlung ausführen und ist kein niedliches Maskottchen. Der ursprüngliche IP-Hinweis und die Namensnennung Ian bleiben bestehen; kennzeichne das Projekt als unabhängige deutsche Ableitung.

## Referenzen nach Bedarf lesen

- `references/style-dna.md`: Bildsprache, Farben und Ausschlüsse.
- `references/xiaohei-ip.md`: Figur, Verhalten und Grenzen.
- `references/composition-patterns.md`: Bildaufbau und neue Metaphern.
- `references/prompt-template.md`: Vorlagen für Bildszenen und Bildkorrekturen.
- `references/qa-checklist.md`: Video- und Bildprüfung.
- `assets/examples/`: nur zur groben visuellen Kalibrierung. Die Beispielgrafiken enthalten chinesische Schrift und sind keine fertigen deutschen Videobilder. Nicht nachzeichnen oder wiederverwenden, sofern der Nutzer es nicht ausdrücklich verlangt.

## Produktionsablauf

### 1. Thema verstehen

Lies die gelieferten Texte, Dateien oder Links, sofern verfügbar. Ermittle:

- Zielgruppe und Vorwissen
- ein konkretes Lernziel
- die zentrale Aussage und die wichtigsten Belege
- Begriffe, die kurz erklärt werden müssen
- Informationen, die fehlen oder unsicher sind

Erfinde keine Tatsachen, Zahlen, Zitate oder Quellen. Wenn Recherche nötig ist, nutze geeignete Quellen und kennzeichne Belege. Bei fehlender Zielgruppe schlage eine plausible vor und markiere die Annahme.

### 2. Deutsches Skript schreiben

Schreibe für das Ohr, nicht als vorgelesenen Fachtext:

- Standardmäßig 60–180 Sekunden; Länge an Wunsch und Thema anpassen.
- Kurzer Einstieg mit Problem oder Frage, dann klare Erklärung, Beispiel und knapper Schluss.
- Natürliche deutsche Satzstellung, aktive Verben, kurze Sätze und verständliche Übergänge.
- Fachbegriffe beim ersten Auftreten knapp erklären; Abkürzungen beim Sprechen ausschreiben, wenn das natürlicher klingt.
- Keine wörtliche Übersetzung, keine chinesischen Einblendungen, außer bei Eigennamen oder ausdrücklich gewünschtem Inhalt.
- Jede Szene erhält einen eigenen Sprechertext. Plane grob 1–2 kurze Sätze pro Szene; Gesamtlänge und Sprechtempo passend halten.

Gib vor der Erzeugung eine knappe Produktionsübersicht aus: Arbeitstitel, Zielgruppe, Lernziel, geschätzte Länge und Szenenzahl. Wenn der Nutzer bereits eine fertige Erzeugung verlangt, nicht auf unnötige Bestätigung warten.

### 3. Storyboard erstellen

Erstelle eine Szene pro Gedankenschritt (typisch 4–8 Szenen). Für jede Szene notiere:

- laufende Nummer und Funktion im Erklärbogen
- exakten deutschen Sprechertext
- kurze deutsche Bildschirmbeschriftung (bevorzugt höchstens 3–6 Wörter)
- Bildidee und die konkrete Handlung von Xiaohei
- optionale Übergangs- oder Bewegungsanweisung
- verwendete Quellen/Fakten, sofern relevant

Die Bildidee soll das Gesagte ergänzen, nicht den vollständigen Sprechertext als Textwand wiederholen. Erfinde für jedes Thema eine neue, passende physische Metapher.

### 4. Szenenbilder erzeugen

Wenn ein Bildgenerator verfügbar ist, erzeuge pro Szene ein einzelnes 16:9-Bild. Keine Collage aus allen Szenen. Verwende `references/prompt-template.md`. Die Bilder müssen den deutschen Begriffsinhalt korrekt darstellen. Begrenze sichtbare Beschriftungen auf kurze, ausdrücklich angegebene deutsche Wörter; lange Texte lieber später als Untertitel ausspielen.

Wenn kein Bildgenerator verfügbar ist, liefere die fertigen Bildprompts und das Storyboard; behaupte nicht, Bilddateien erzeugt zu haben.

### 5. Sprecher-Audio erstellen

Nutze eine verfügbare TTS-Funktion mit deutscher Stimme, deutlicher Aussprache, ruhigem natürlichem Tempo und neutraler Emotion. Erzeuge eine Sprachdatei pro Szene (WAV, MP3 oder ein von FFmpeg lesbares Audioformat), damit jede Szenenlänge sauber bestimmbar ist. Keine Stimme imitieren, für die keine Berechtigung vorliegt. Hintergrundmusik standardmäßig weglassen; nur lizenzierte oder ausdrücklich bereitgestellte Musik verwenden.

Wenn kein TTS-Werkzeug verfügbar ist, liefere das deutsche Sprecher-Manuskript und benenne klar, dass noch Audioaufnahmen fehlen. Niemals Platzhalter oder stumme MP4s als fertiges Video ausgeben.

### 6. Projektdatei und Rendern

Erstelle eine Projektdatei gemäß `templates/video-project.example.json`. Alle Bild- und Audiopfade sind relativ zum Speicherort der Projektdatei. Pro Szene braucht der Renderer:

- `image`: Pfad zum Szenenbild
- `audio`: Pfad zur deutschen Sprachaufnahme dieser Szene
- `subtitle`: kurze deutsche Untertitelzeile für die Szene

Rendere aus dem Repository-Stammverzeichnis:

```bash
python3 scripts/render_video.py PFAD/ZUM/video-project.json --output PFAD/ZUM/erklaervideo.mp4
```

Wenn der Skill außerhalb des geklonten Repositories installiert ist, rufe das darin enthaltene `scripts/render_video.py` mit seinem vollständigen Pfad auf. Der Renderer legt eine gleichnamige `.srt`-Datei an. Er benötigt `ffmpeg` und `ffprobe`. Wenn sie fehlen oder ein Renderfehler auftritt, zeige den tatsächlichen Fehler und liefere kein erfundenes Erfolgsergebnis.

### 7. Prüfung und Übergabe

Prüfe Skript, Fakten, deutsche Rechtschreibung, Szenenreihenfolge, Audiodateien, SRT-Zeitangaben, Bildformat und Videoausgabe anhand von `references/qa-checklist.md`. Spiele das Video bzw. prüfe mindestens Streams und Dauer mit `ffprobe`, sofern die Werkzeuge verfügbar sind.

Nenne bei der Übergabe nur überprüfte Ergebnisse: Video- und Untertitelpfad, Dauer, Szenenzahl, verwendete Assets und offene Punkte. Trenne erzeugte Dateien von Prompts oder noch fehlenden Inputs.

## Standard-Videostil

- 16:9, weißer Hintergrund, schwarzes feines Handlinienbild, großzügige Leerräume.
- Xiaohei handelt im Bild an einem konkreten Teil des Systems.
- Rot für Warnung/Ergebnis, Orange für Bewegungsfluss, Blau sparsam für Zusatzinformation.
- Pro Szene eine visuelle Aussage, wenige Elemente, keine überladenen Folien.
- Übergänge schlicht halten; ruhige Schnitte oder sanfte Überblendungen nur, wenn verfügbar.
- Gut lesbare deutsche Untertitel aus der SRT-Datei; nicht auf zuverlässige deutsche Bildtext-Erzeugung durch das Bildmodell vertrauen.

## Ausgabe, wenn noch keine Medien erzeugt werden können

Wenn Bild- oder Sprachwerkzeuge fehlen, trotzdem die verwertbaren Bestandteile erstellen: deutsches Skript, Szenen-Storyboard, Bildprompts und JSON-Gerüst. Weise ausdrücklich darauf hin, welche Assets noch benötigt werden, damit das Video gerendert werden kann.
