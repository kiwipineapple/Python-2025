# singledispatchmethod ist ein Decorator (Funktion) aus dem functools-Modul.
# Er ermöglicht es, Methoden zu definieren, die je nach Typ des ersten Arguments
# unterschiedliche Implementierungen aufrufen.
# Dadurch lässt sich typbasierter Polymorphismus in Klassenmethoden umsetzen.

from functools import singledispatchmethod

# Wir definieren eine Klasse namens Printer
class Printer:

    # Dank des Decorators @singledispatchmethod kann die Methode anzeigen() automatisch erkennen,
    # welchen Datentyp sie bekommen hat, und entsprechend die passende Version ausführen.
    # Das bedeutet: Sie kann für verschiedene Datentypen unterschiedlich reagieren.
    @singledispatchmethod
    def anzeigen(self, arg):
        # Standardverhalten: wenn kein spezieller Typ erkannt wird
        print(f"Standardverhalten für Typ: {type(arg)}")


    # @anzeigen.register registriert eine spezielle Variante der Methode "anzeigen"
    # für den Typ int. Das bedeutet: Wenn ein int übergeben wird, wird diese Variante aufgerufen.
    # Der Funktionsname "_" ist nur ein Platzhalter. Der Name ist nicht wichtig,
    # weil die Methode über den Typ gefunden wird – nicht über ihren Namen.
    @anzeigen.register
    def _(self, arg: int):
        print("Verarbeitung für Integer:", arg)

    # Diese Variante wird aufgerufen, wenn ein String (str) übergeben wird.
    @anzeigen.register
    def _(self, arg: str):
        print("Verarbeitung für String:", arg)

# Wir erstellen ein Objekt der Klasse Printer
p = Printer()

# Wir rufen die Methode "anzeigen" mit verschiedenen Typen auf:

p.anzeigen(42)         # Das ist ein int → Ausgabe: Verarbeitung für Integer: 42
p.anzeigen("Hallo")    # Das ist ein str → Ausgabe: Verarbeitung für String: Hallo
p.anzeigen(3.14)       # Das ist ein float → kein spezieller Fall definiert,
                       # → daher Standardverhalten: Typ: <class 'float'>
