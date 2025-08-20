class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __str__(self):
        # Wird aufgerufen, wenn print(hund) oder str(hund) verwendet wird– benutzerfreundlich
        return f"{self.name} ist {self.alter} Jahre alt."

    def __repr__(self):
        # Wird im Debugger, in Listen, bei repr(hund) oder bei fehlendem __str__ verwendet
        return f"Hund(name='{self.name}', alter={self.alter})"

# Objekt erstellen
h = Hund("Bello", 5)

# __str__ wird bei print() verwendet
print(h) # Ausgabe: Bello ist 5 Jahre alt.
print(str(h)) # wie
print(str(5))


# Direkter Aufruf von repr() → verwendet __repr__
print(repr(h))  # Ausgabe: Hund(name='Bello', alter=5)

# Verwendung in einer Liste → Python verwendet automatisch __repr__, nicht __str__
hunde = [h]
print(hunde)
# Ausgabe: [Hund(name='Bello', alter=5)]



"""
# Erklärung:
# Wenn ein Objekt (wie 'h') in einer Liste steckt und du die Liste ausgibst,
# ruft Python für jedes Element in der Liste die __repr__-Methode auf – nicht __str__.
# Grund: __repr__ soll eine möglichst genaue und technische Darstellung liefern,
# die z.B. für Debugging oder Wiederherstellung (repr -> eval) geeignet ist.

# str(h) wird also NICHT verwendet – selbst wenn __str__ vorhanden ist.
# Nur repr(h) wird genutzt, wenn das Objekt Teil einer Datenstruktur wie Liste, Dict oder Set ist.
"""


"""
__str__ = für Menschen → schön lesbar
__repr__ = für Entwickler → technisch, nützlich für Debugging

# Hinweis:
# Wenn __str__ NICHT definiert ist, verwendet Python automatisch __repr__ als Ersatz.
"""