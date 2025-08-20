class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __str__(self):
        return f"{self.name} ist {self.alter} Jahre alt."

    def __repr__(self):
        return f"Hund(name='{self.name}', alter={self.alter})"




# Objekt erstellen
h = Hund("Bello", 5)
print("Fertig")  # → Breakpoint hier setzen



"""
Starte das Programm im Debug-Modus
Rechts oben auf den kleinen Käfer (Debug-Symbol) klicken.

Schaue unten in die Variablenansicht
Dort siehst du:
h = Hund(name='Bello', alter=5)
→ das ist die Ausgabe von __repr__


PyCharm ruft automatisch __repr__() auf, um das Objekt darzustellen.
Auch wenn __str__ da ist, benutzt der Debugger immer __repr__, weil er Entwicklern beim Verständnis helfen soll

Der Debugger braucht eine technisch vollständige, genaue Darstellung – deshalb immer __repr__, nie __str__.

"""


