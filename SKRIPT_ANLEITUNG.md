# GitHub-Profil-Header

`generate_header.py` erzeugt den blauen SVG-Header mit Rakete, Profiltext, dem vorhandenen Bild aus `profile.png` und der animierten Commit-Schlange.

## Lokal erzeugen

```bash
python generate_header.py
```

Das Skript schreibt `header.svg`. Wenn `dist/github-snake.svg` vorhanden ist, nutzt es diese Datei. Andernfalls lädt es die zuletzt veröffentlichte Schlange aus dem `output`-Branch. Für diesen lokalen Fall ist eine Internetverbindung nötig.

Die Texte und Badges stehen im `CONFIG`-Block von `generate_header.py`. Ein neues Profilbild kann später durch Austausch von `profile.png` eingebaut werden. Weitere Python-Pakete sind für den Generator nicht nötig.

## Automatische Aktualisierung

Der Workflow `.github/workflows/snake.yml` generiert die blaue Schlange und den Header bei Pushes auf `main`, täglich und auf manuellen Aufruf. Beide SVGs landen im `output`-Branch, aus dem `README.md` den Header lädt.
