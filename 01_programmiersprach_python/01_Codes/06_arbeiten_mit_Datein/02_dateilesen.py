import os
from pathlib import Path
os.chdir(Path(__file__).parent)

# Variante 1: Datei manuell im Schreibmodus öffnen und schließen
# 'r' steht für (lesen) read

file = open('beispiel.txt', 'r', encoding='UTF-8')
content = file.read()
print(content)
file.close()

print('*'*40)

# variante 2
with open('beispiel1.txt', 'r', encoding='UTF-8') as file:
    content = file.read()
    print(content)

print('*'*40)

# variante 3: Datei Zeile für Zeile lesen
with open('beispiel1.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        print(line.strip())