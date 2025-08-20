class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        # return "meaw"

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
        # __str__ Methode gibt dieses Objekt in einer lesbaren Form aus


v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)
# + Operatorüberladung (operator overloading) Beispiel
# dies gibt ein neues Objekt zurück


print(v1 * v2)
# * Operatorüberladung (operator overloading) Beispiel
# dies gibt ein neues Objekt zurück
