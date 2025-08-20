"""
Stell dir vor, du entwickelst ein Modul für einen Webshop.
Ein Kunde soll auf einen Artikel einen prozentualen Rabatt bekommen – z.B. 10%.

Du möchtest eine Klasse RabattRechner erstellen, die sich wie ein Rabattwerkzeug verhält:
Man gibt ihr beim Erstellen den Rabattwert in Prozent mit,
und später kann man mit ihr den neuen Preis berechnen – indem man sie einfach wie eine Funktion aufruft.

rechner = RabattRechner(10)    # 10 % Rabatt
print(rechner(50))             # Erwartet: 45.0

Anforderungen:
Die Klasse soll beim Erstellen den Rabatt in Prozent speichern (z.B. 10).

Später soll man das Objekt mit einem Preis „aufrufen“ können – so als ob man eine Funktion schreibt
– und den reduzierten Preis als Ergebnis bekommen.

Die Klasse darf nicht einfach eine Methode wie berechne(...) verwenden. Stattdessen soll das
Objekt direkt „benutzbar wie eine Funktion“ sein.
"""


class RabattRechner:
    def __init__(self, rabatt) -> None:
        self.rabatt = rabatt
