# Beispielprompts

Die folgenden deutschen Prompts können in einem geeigneten Agenten verwendet werden. Die Verfügbarkeit von Bild- und Sprachfunktionen hängt vom Agenten ab.

## Erst das Skript und Storyboard planen

```text
Nutze $xiaohei-erklaervideos. Erzeuge noch keine Medien.
Analysiere dieses Thema für ein deutsches Erklärvideo. Nenne Zielgruppe, Lernziel und eine plausible Dauer. Schreibe dann ein natürlich gesprochenes Skript und ein Storyboard mit 5 Szenen. Für jede Szene: Sprechertext, kurze deutsche Einblendung, Bildidee und konkrete Handlung von Xiaohei.

<THEMA ODER TEXT>
```

## Ein vollständiges Erklärvideo erstellen

```text
Nutze $xiaohei-erklaervideos und erstelle aus diesem Text ein vollständiges deutsches Erklärvideo.
Schreibe den Sprechertext natürlich und verständlich, erzeuge ein Storyboard, pro Szene ein eigenes Bild und deutsche Sprachaufnahmen. Rendere MP4 und SRT, sofern Bild- und TTS-Werkzeuge sowie FFmpeg verfügbar sind. Wenn ein Werkzeug fehlt, sage genau, welche Dateien noch fehlen.

<THEMA ODER TEXT>
```

## Längeren Artikel verdichten

```text
Nutze $xiaohei-erklaervideos. Verdichte diesen langen Artikel zu einem Erklärvideo von etwa 2 Minuten. Übernimm nur die wichtigsten Aussagen, bewahre Einschränkungen und Belege und erfinde keine Fakten. Gib zuerst ein Skript und Storyboard mit 6-8 Szenen aus; noch keine Medien.

<ARTIKEL>
```

## Eine Szene illustrieren

```text
Erzeuge ein einzelnes 16:9-Szenenbild im Xiaohei-Stil für dieses Video.
Kernaussage: Eine gute Rückmeldung zeigt nicht nur, was schiefging, sondern auch den nächsten sinnvollen Schritt.
Xiaohei soll den nächsten Schritt aus einer seltsamen Maschine herausreichen. Weißer Hintergrund, schwarze feine Handzeichnung, wenig Rot/Orange/Blau. Nur die kurzen deutschen Bildwörter „Fehler“ und „Nächster Schritt“ verwenden. Keine zusätzlichen Beschriftungen.
```

## Sprechertext überarbeiten

```text
Überarbeite diesen Text für eine deutsche Sprecheraufnahme: natürliche gesprochene Sprache, kurze Sätze, keine unnötigen Anglizismen, Fachbegriffe beim ersten Auftreten kurz erklären. Erhalte Fakten, Zahlen, Einschränkungen und Quellen unverändert. Teile den Text in kurze Szenen und gib pro Szene eine passende kurze deutsche Untertitelzeile aus.

<SPRECHERTEXT>
```

## Fehlende Medien als Projektgerüst vorbereiten

```text
Nutze $xiaohei-erklaervideos. Erstelle ein deutsches Skript und Storyboard sowie eine gültige video-project.json mit deutschen Szenen-Untertiteln. Erzeuge keine Platzhalter-Medien. Liste die erforderlichen Bild- und Audiodateien genau auf.

<THEMA>
```
