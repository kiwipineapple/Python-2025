class Beispiel:
    @staticmethod
    def anzeigen(*args):
        # Je nach Anzahl der übergebenen Argumente reagiert die Methode unterschiedlich
        if len(args) == 2:
            print("Methode Reaktion Typ 1 (zwei Argumente)")
        elif len(args) == 1:
            print("Methode Reaktion Typ 2 (ein Argument)")
        elif len(args) == 0:
            print("Methode Reaktion Typ 3 (kein Argument)")
        else:
            print("Methode Reaktion Typ 4 (mehr als zwei Argumente)")

# Aufrufe:
Beispiel.anzeigen(10, 20)     # Ausgabe: Typ 1
Beispiel.anzeigen(42)         # Ausgabe: Typ 2
Beispiel.anzeigen()           # Ausgabe: Typ 3
Beispiel.anzeigen(1, 2, 3)    # Ausgabe: Typ 4
