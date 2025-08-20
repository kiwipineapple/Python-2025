"""
(LEICHT)

Aufgabe: Punktestand

Schreibe eine Klasse Spieler. Ein Spieler hat einen Namen und eine Punktzahl.

Die Punktzahl darf nie negativ sein. Wenn man versucht, eine negative Punktzahl zu setzen,
soll ein ValueError ausgelöst werden.

Beispiel:

s = Spieler("Anna")
s.punkte = 10
print(s.punkte)  # 10

s.punkte = -5    # ValueError!
"""


class Spieler:
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def punkte(self):
        return self._punkte

    @punkte.setter
    def punkte(self, neu_punkte):
        if neu_punkte < 0:
            raise ValueError('Punktzahl is negativ!')
        self._punkte = neu_punkte


s = Spieler("Anna")
s.punkte = 19
print(s.punkte)
