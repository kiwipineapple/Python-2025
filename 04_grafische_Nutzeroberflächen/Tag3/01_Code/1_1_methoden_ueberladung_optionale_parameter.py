class Beispiel:
    @staticmethod
    def anzeigen(a=None, b=None):
        if a is not None and b is not None:
            print("Methode Reaktion Typ 1")
        elif a is not None:
            print("Methode Reaktion Typ 2")
        elif b is not None:
            print("Methode Reaktion Typ 3")
        else:
            print("Methode Reaktion Typ 4")


Beispiel.anzeigen(10, 20)
Beispiel.anzeigen(10)
Beispiel.anzeigen(b=6)
Beispiel.anzeigen()
