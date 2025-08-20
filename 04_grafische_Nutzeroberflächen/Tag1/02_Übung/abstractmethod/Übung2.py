from abc import ABC, abstractmethod


class Tier(ABC):
    @abstractmethod
    def laut(self):
        pass

    @abstractmethod
    def bewegung(self):
        pass


class Hund(Tier):
    def laut(self):
        return "Wau"

    def bewegung(self):
        return "Hund läuft schnell."


f = Hund()
# f.laut(zeit='am Morgen')
print(f.laut())
print(f.bewegung())
