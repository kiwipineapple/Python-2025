"""

class Zahl:
    def __init__(self, wert):
        self.wert = wert

    def __add__(self, other):
        return 100

    def __str__(self):
        return f"meaw"

z1 = Zahl(5) # 5
z2 = Zahl(7) # 7

print(z1 + z2) # ?

print(z1) # ?


"""

class Zahl:
    def __init__(self, wert):
        self.wert = wert

    def __add__(self, x):
        # Wird aufgerufen, wenn man z.B. z1 + z2 schreibt
        print(self.wert)
        print(x.wert)
        return Zahl( self.wert + x.wert  )
        #  5 + 7 beide int  --> add methode in int Klasse  --> 12
        # Zahl(12)

    def __str__(self):
        # Für die lesbare Darstellung bei print()
        return f"Zahl({self.wert})"

z1 = Zahl(5)
z2 = Zahl(7)

# z1 - z2  __sub__,
# z1 * z2 __mul__,
#!= __ne__

z3 = z1 + z2 # z3 = Zahl(12)
print(z3)  # Ausgabe: Zahl(12)






"""

"""