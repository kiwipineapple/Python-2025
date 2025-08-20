class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magische Methode zur Überladung des + Operators
    def __add__(self, other):
        return Punkt(self.x + other.x, self.y + other.y)

    # Für lesbare Ausgabe bei print()
    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

# Zwei Punkt-Objekte
p1 = Punkt(3, 4)
p2 = Punkt(1, 2)

# Verwendung des + Operators → ruft intern p1.__add__(p2) auf
p3 = p1 + p2

print(p3)  # Ausgabe: Punkt(4, 6)
