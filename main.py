from pathlib import Path

# 1. Projektordner und Notizordner bestimmen
project_dir = Path(__file__).resolve().parent
notes_dir = Path(r"C:\Users\moham\Documents\MohammadValut\MohammadValut")

print("Notizordner:", notes_dir)

# 2. Prüfen, ob der Ordner vorhanden ist
if not notes_dir.is_dir():
    raise FileNotFoundError(f"Notizordner nicht gefunden: {notes_dir}")

# 3. Markdown-Dateien einschließlich Unterordnern suchen
markdown_files = []

for path in notes_dir.rglob("*.md"):
    if path.is_file():
        markdown_files.append(path)

# 4. Anzahl und Dateipfade anzeigen
print(f"\nGefundene Markdown-Dateien: {len(markdown_files)}")

for path in sorted(markdown_files):
    print("-", path.relative_to(notes_dir))