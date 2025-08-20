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


"""


class Rechteck:
    def __init__(self, b: int, h: int) -> None:
        self.b = b
        self.h = h

    def get_area(self) -> int:
        area = self.__new_b * self.__new_b
        return area

    def breite(self, b: int):
        if b < 0:
            raise ValueError()
        self.__new_b = b

    def hoehe(self, h: int):
        if h < 0:
            raise ValueError()
        self.__new_b = h


r1 = Rechteck(10, 15)
# r1.breite(2)
print(r1.get_area())
