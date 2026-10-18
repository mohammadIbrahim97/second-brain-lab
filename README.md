# Second Brain Lab

Ein Lernprojekt fuer Python, neuronale Netze und ein persoenliches Wissenssystem mit Obsidian.

## Aktueller Stand

Das Python-Programm findet Markdown-Dateien (`.md`) in einem Obsidian-Vault, einschliesslich der Unterordner. Es zeigt die Anzahl und die relativen Dateipfade an. Die Notizen werden dabei nicht veraendert.

## Einrichtung unter Windows

Voraussetzung: Python 3.13.

Im Projektordner eine virtuelle Umgebung erstellen:

```powershell
py -3.13 -m venv .venv
```

In `main.py` die Variable `notes_dir` auf den eigenen Obsidian-Ordner setzen:

```python
notes_dir = Path(r"C:\Pfad\zum\Obsidian-Vault")
```

Anschliessend das Programm starten:

```powershell
.\.venv\Scripts\python.exe .\main.py
```

Die aktuelle Version verwendet ausschliesslich die Python-Standardbibliothek. Es muessen keine zusaetzlichen Pakete installiert werden.

## Geplante Schritte

- Texte einlesen und Metadaten erfassen.
- Obsidian-Links erkennen und eine Suche aufbauen.
- Kleine eigene Sprachmodelle trainieren und auswerten.
- Erst nach den Grundlagen optional ein fertiges Sprachmodell anbinden.

## Lokale Daten

Die virtuelle Umgebung, der lokale Ordner `data/` und `.env`-Dateien sind durch `.gitignore` vom Versionsverlauf ausgeschlossen. Der Obsidian-Vault liegt ausserhalb des Projektordners und wird nicht in dieses Repository kopiert.
