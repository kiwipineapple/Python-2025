eingaben = [] # Liste für alle Eingaben (nicht benutzt, optional)
unique = [] # Liste für eindeutige Werte
while True:
    zahl = int(input("> ")) # Zahl eingeben
    if zahl == 0: # Bei 0 Schleife beenden
        break
    if zahl not in unique: # Nur hinzufügen, wenn noch nicht vorhanden
        unique.append(zahl)
# Ausgabe der eindeutigen Werte
print("Einzigartige Werte:", end=" ")
for z in unique:
    print(z, end=" ")
print()