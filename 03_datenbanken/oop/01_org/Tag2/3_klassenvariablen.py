"""
Klassen-Variablen (Klassenattribute)

Klassenattribute können NUR von der Klasse verändert werden.
Sie können aber von Objekten gelesen werden.
"""


class Robot:
    # Zählt die Anzahl der AKTIVEN Roboter Instanzen
    population = 0

    def __init__(self, name: str):
        self.name = name
        Robot.population += 1  # Klasssenvariable population um 1 erhöhen
        self._running = True  # Roboter startet bei Instanziierung des Objekts

    def __del__(self) -> None:
        """Wird immer ausgeführt, wenn die Instanz gelöscht wird via del.

        Falls durch eine Zuweisung zwei Referenzen exisitieren, wird del
        erst aufgerufen, wenn alle Referenzen zerstört sind.
        """
        print("Del wird ausgeführt")
        Robot.population -= 1

    def set_off(self):
        if self._running:
            print("Roboter wird abgeschaltet")
            self._running = False
            Robot.population -= 1
        else:
            print("Roboter ist schon aus.")

    def set_on(self):
        if self._running:
            print("Roboter ist schon aktiv.")
        else:
            print("Roboter wird gestartet")
            self._running = True
            Robot.population += 1


r2d2 = Robot("R2D2")
print(r2d2.population)  # liest Klassenvariable population
print(r2d2.__dict__)  # {'name': 'R2D2'}

c3po = Robot("C3PO")
print(c3po.population)  # # liest Klassenvariable population
print(c3po.__dict__)  # {'name': 'C3PO'}
c3po.set_off()
c3po.set_on()

c3po_copy = c3po
del c3po  # ruft __del__ auf (nur wenn c3po die einzige Referenz ist)

print("Anzahl der aktiven Roboter:", Robot.population)
