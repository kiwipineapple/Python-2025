class Spieler:
    def __init__(self, name):
        self.name = name
        self.punkte = 0

    @property
    def punkte(self):
        return self._punkte

    @punkte.setter
    def punkte(self, wert):
        if wert < 0:
            raise ValueError("Punkte dürfen nicht negativ sein.")
        self._punkte = wert


# Beispiel:
s = Spieler("Anna")
s.punkte = 10
print(s.punkte)  # 10

# s.punkte = -5  # Das würde einen Fehler auslösen
