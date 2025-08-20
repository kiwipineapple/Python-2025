import os
from pathlib import Path
os.chdir(Path(__file__).parent)


# Variante 1: Datei manuell im Schreibmodus öffnen und schließen
# 'w' steht für (Schreiben) Write

file = open('beispiel.txt', 'w', encoding='UTF-8')
file.write('Das ist der erste Satz\n')
file.write('Das ist der zweite Satz\n')
file.write('''Das ist der dritte Satz
Hallo
by''')
file.close()


# variante 2
with open('beispiel1.txt', 'w', encoding='UTF-8') as file:
    file.write('Das ist der zweiten Satz\n')
    file.write("""Das ist der drittenSatz
Hallo
by""")
# Nach dem 'with'-Block wird die Datei automatisch geschlossen