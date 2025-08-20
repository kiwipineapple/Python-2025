"""
  Schleifenarten in Python:

- for-Schleifen sind ideal für durchlaufbare Datenstrukturen,
  wenn die Anzahl der Iterationen bekannt ist.

- while-Schleifen sind nützlich für Bedingungen, bei denen
  die Iteration von einer logischen Prüfung abhängt und
  nicht von einer festen Anzahl.
"""
# Beispiel 1: Endliche while-Schleife (gesteuert durch eine Bedingung)

temperature = 35
while temperature > 30:
    print('Klima an', temperature)
    temperature -= 1 #   temperature  =   temperature  - 1

print('Fertig')    


#  Beispiel 2: Interaktive while-Schleife (Benutzereingabe)

command = ""
while command != 'exit':
    command = input('> ')
    print('Echo', command)

print('Fertig')      

# Hinweis:
# Eine while-Schleife kann auch endlos laufen, wenn die Bedingung nie falsch wird:
# Beispiel (nicht ausführen, Endlosschleife!):
while True:
    print("Läuft unendlich...")  # Mit Ctrl+C abbrechen




