class SpielObjekt:
    def update(self):
        raise NotImplementedError("Subclasses should implement this!")


class Spieler(SpielObjekt):
    def update(self):
        return "Spieler aktualisiert"


class Gegner(SpielObjekt):
    def update(self):
        return "Gegner aktualisiert"


class Hindernis(SpielObjekt):
    def update(self):
        return "Hindernis aktualisiert"


objekte = [Spieler(), Gegner(), Hindernis()]
for obj in objekte:
    print(obj.update())
