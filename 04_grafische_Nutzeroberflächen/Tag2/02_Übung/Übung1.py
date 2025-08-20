class Vektor:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vektor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vektor(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vektor(self.x * scalar, self.y * scalar)

    def __repr__(self) -> str:
        return f'Vektor({self.x}, {self.y})'


r1 = Vektor(1, 3)
r2 = Vektor(4, 5)
# print(r1 - r2)

# print(r1 * 2)
print(r1)  # __repr__ wird aufgerufen
