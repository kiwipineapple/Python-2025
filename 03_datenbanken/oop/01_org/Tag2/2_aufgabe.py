"""
Erstelle eine Klasse Rechteck mit den Attributen breite und hoehe.
Die Klasse benötigt eine Methode area, die die Fläche ausrechnet und zurückgibt.

breite darf nicht < 0 sein: ValueError
hoehe darf nicht < 0 sein: ValueError

r1 = Rechteck(breite=10, hoehe=13)
r1.hoehe = 3
print(r1.area()) # 30

r1.hoehe = -12 # ValueError
r2 = Rechteck(breite=10, hoehe=-1)
ValueError!

Happy Coding! Kein Copy & Paste!

"""


class Rechteck:
    def __init__(self, breite: int, hoehe: int):
        self.breite = breite
        self.hoehe = hoehe

    @property
    def breite(self):
        return self._breite

    @breite.setter
    def breite(self, value: int):
        if value < 0:
            raise ValueError("Breite darf nicht negativ sein.")
        self._breite = value

    @property
    def area(self) -> int:
        return self.breite * self.hoehe


r1 = Rechteck(breite=10, hoehe=13)
print(r1.area)
