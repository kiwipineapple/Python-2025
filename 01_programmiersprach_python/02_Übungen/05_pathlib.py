# Aufgabenstellung
# Schreibe ein Python-Programm mit pathlib, das folgendes tut:
# 1. Erstelle einen Ordner kaputte_dateien/ (falls nicht vorhanden).
# 2. Erstelle in diesem Ordner einige Beispiel-Dateien mit der Endung .py.sec (z. B. datei1.py.sec,
# datei2.py.sec).
# 3. Erstelle außerdem einen Ordner richtige_dateien/.
# 4. Liste alle Dateien in kaputte_dateien/ auf.
# 5. Verwende .stem, um den Dateinamen ohne die Endung .sec zu erhalten.
# 6. Benenne jede Datei um, entferne die kaputte Endung .sec und speichere die neue Datei mit der
# Endung .py im Ordner richtige_dateien/.
# Ziel
# Nach dem Skript sollen z. B. aus kaputte_dateien/datei1.py.sec → richtige_dateien/datei1.py
# werden.
# Hinweis: Verwendet nur pathlib-Funktionen wie mkdir(), touch(), .stem und rename().

import os
from pathlib import Path
os.chdir(Path(__file__).parent)

aktuell_pfad = Path.cwd()
ordner = aktuell_pfad / 'kaputte_dateien'
ordner.mkdir(exist_ok=True)

datei1 = ordner / 'datei1.py.sec'
datei2 = ordner / 'datei2.py.sec'
datei1.touch()
datei2.touch()

file = open('datei1.py.sec', 'w', encoding='UTF-8')
file.write('Hallo world!')
file.close()

ordner2 = aktuell_pfad / 'richtige_dateien'
ordner2.mkdir(exist_ok=True)

print('datei1 name: ', datei1.name)
print('datei2 name: ', datei2.name)

neu_datei1 = datei1.stem
neu_datei2 = datei2.stem
print(neu_datei1, neu_datei2)
print(Path.cwd())

aktuell_pfad = Path.cwd() / 'richtige_dateien'
neu_path1 = aktuell_pfad / neu_datei1
neu_path1.touch()

neu_path2 = aktuell_pfad / neu_datei2
neu_path2.touch()


