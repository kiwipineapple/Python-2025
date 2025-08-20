"""(MITTEL)
Erstelle eine Klasse Kreis mit der Eigenschaft radius, x und y Koordinate im
kart. Koordinatensystem.
Erstelle zwei Instanzen dieser Klasse auf Basis einer Usereingabe (input).

Prüfe, ob sich die Kreise schneiden / überlagern oder nicht.
Wir gehen von legalen Eingaben aus, d. h. der Radius ist immer größer als 0.

# User-Beispiel:

Bitte gebe den Radius, X und Y Koordinate des ersten Kreises ein:
10.3, 23, 14

Bitte gebe den Radius, X und Y Koordinate des zweiten Kreises ein:
4, 12, 55

Die Kreise kollidieren nicht.

Wollen Sie eine weitere Kollision überprüfen? J/N

Hinweis: Es reicht eine einfache Kollisionserkennung zu implementieren.

# Code-Beispiel


class Circle:
    ...

def main():
    # input("Bitte gebe den Radius, X und Y Koordinate des ersten Kreises ein: ")
    circle_1 = Circle(radius=r, x=x, y=y)

    # input("Bitte gebe den Radius, X und Y Koordinate des ersten Kreises ein: ")
    circle_2 = Circle(radius=r, x=x, y=y)

    # Prüfe, ob sich Kreise schneiden / überlagern ...
    # Ausgabe: "Die Kreise kollidieren." oder "Die Kreise kollidieren nicht."

    # Weitere Prüfung? Y/N?

"""
import math
import matplotlib.pyplot as plt


class Circle:
    def __init__(self, radius, x, y) -> None:
        self.radius = radius
        self.x = x
        self.y = y

    def check_kollision(self, circle):
        disstance = math.sqrt((self.x - circle.x) **
                              2 + (self.y - circle.y) ** 2)
        sum_radius = self.radius + circle.radius

        if disstance < sum_radius:
            print(f'Die Kreise kollidieren.')
        else:
            print(f'Die Kreise kollidieren nicht.')


def main():
    while True:
        r1, x1, y1 = input(
            "Bitte gebe den Radius, X und Y Koordinate des ersten Kreises ein: ").split(',')
        r1 = float(r1)
        x1 = float(x1)
        y1 = float(y1)
        circle_1 = Circle(radius=r1, x=x1, y=y1)

        r2, x2, y2 = input(
            "Bitte gebe den Radius, X und Y Koordinate des ersten Kreises ein: ").split(',')
        r2 = float(r2)
        x2 = float(x2)
        y2 = float(y2)
        circle_2 = Circle(radius=r2, x=x2, y=y2)

        circle_1.check_kollision(circle_2)

        weiter = input('Weitere Prüfung? (J/N) ').lower()

        if weiter == 'n':
            break


if __name__ == "__main__":
    main()
