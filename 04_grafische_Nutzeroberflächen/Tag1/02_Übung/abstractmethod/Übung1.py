from abc import ABC, abstractmethod
import math


class Form(ABC):
    @abstractmethod
    def fläche(self):
        pass


class Kreis(Form):
    def __init__(self, r) -> None:
        self.radius = r

    def fläche(self):
        return math.pi * pow(self.radius, 2)


f = Kreis(5)
print("Die Fläche für Kreis r = 5 ist:", f.fläche())
