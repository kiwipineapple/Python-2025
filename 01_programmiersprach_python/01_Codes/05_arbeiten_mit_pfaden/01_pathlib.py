
# pathlib 
# ============================
# Dieses Skript zeigt, wie man mit pathlib arbeitet: Verzeichnisse anzeigen,
# Ordner und Unterordner erstellen, Dateien anlegen und Informationen abfragen.

import os
from pathlib import Path

# Arbeitsverzeichnis auf Skript-Ordner setzen
os.chdir(Path(__file__).parent)

# 1. Aktuelles Arbeitsverzeichnis anzeigen
aktueller_pfad = Path.cwd()
print("Aktuelles Verzeichnis:", aktueller_pfad)

# 2. Neuen Ordner erstellen
ordner = aktueller_pfad / "MeinOrdner"
ordner.mkdir(exist_ok=True)
print("Ordner erstellt:", ordner)

# 3. Unterordner im neuen Ordner erstellen
unterordner = ordner / "Unterordner"
unterordner.mkdir(exist_ok=True)
print("Unterordner erstellt:", unterordner)

# # 4. Mit parent den übergeordneten Ordner anzeigen
# print("Parent von Unterordner:", unterordner.parent)

# 5. Neue Datei im Unterordner erstellen
neue_datei = unterordner / "datei.txt"
neue_datei.touch()
print("Datei erstellt:", neue_datei)

# 6. Noch eine Datei im Hauptordner erstellen
neue_datei2 = ordner / "datei2.txt"
neue_datei2.touch()
print("Datei2 erstellt:", neue_datei2)

# 7. Existiert die Datei?
print("Existiert die Datei?", neue_datei.exists())

# 8. Ist es eine Datei?
print("Ist es eine Datei?", neue_datei.is_file())

# 9. Ist es ein Ordner?
print("Ist es ein Ordner?", unterordner.is_dir())

# 10. Dateiname anzeigen
print("Dateiname:", neue_datei.name)

# 11. Pfad als Tupel anzeigen
print("Pfad als Tupel:", neue_datei.parts)

# 12. Dateiname ohne Endung
print("Dateiname ohne Erweiterung:", neue_datei.stem)
