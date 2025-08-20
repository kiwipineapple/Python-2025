# Thema: join()-Funktion in Python
# Was ist das?
# Die join()-Funktion verbindet mehrere Strings aus einer iterierbaren Sammlung (z.B. Liste, Tupel, Set oder auch ein einzelner String) zu einem einzigen neuen String.
# Man legt vorher fest, welches Zeichen (z.B. Leerzeichen, Komma oder Bindestrich)
# zwischen den Elementen stehen soll.

# Beispiel 1: Wörter mit Leerzeichen verbinden
woerter = ["Python", "macht", "Spaß"]
satz = " ".join(woerter)  # Alle Wörter werden mit einem Leerzeichen verbunden
print("Satz:", satz)

# Beispiel 2: Zeichen mit Bindestrich verbinden
zeichen = ["A", "B", "C", "D"]
verbunden = "-".join(zeichen)
print("Mit Bindestrich verbunden:", verbunden)

# Beispiel 3: Liste von Zahlen zuerst in Strings umwandeln
zahlen = [1, 2, 3]
zahlen_strings = []  # Leere Liste für Strings

# Schleife: Jede Zahl in einen String umwandeln und zur Liste hinzufügen
for zahl in zahlen:
    zahlen_strings.append(str(zahl))

# Jetzt die String-Liste mit Komma verbinden
ergebnis = ",".join(zahlen_strings)
print("Zahlen mit Komma:", ergebnis)


# Das "".join() ist ein sehr typischer und effizienter Weg in Python,
# um eine Liste von Strings ohne Trennzeichen zu einem einzigen String zusammenzusetzen.
# Wir haben einzelne Buchstaben in einer Liste
buchstaben = ["P", "y", "t", "h", "o", "n"]

# Wir wollen daraus einen einzigen String machen – ohne Trennzeichen
wort = "".join(buchstaben)

print("Wort:", wort)  # Ausgabe: Python








# Andere Iterierbare objekte
print("-".join(("A", "B", "C")) ) # Tuple

print(",".join({"Apfel", "Banane", "Orange"})) # SET


# Ein String ist auch eine Sammlung von Zeichen (also iterierbar)
text = "ABC"

# join() setzt zwischen jedes Zeichen einen Punkt
ergebnis = ".".join(text)

print("Ergebnis:", ergebnis)  # Ausgabe: A.B.C

