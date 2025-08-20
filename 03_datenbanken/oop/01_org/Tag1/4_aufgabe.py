"""
Aufgabe:
Erstellt eine Klasse City mit den Attributen name und population
und erstellt davon zwei Instanzen munich und hamburg.
Setzt die Attribute mit entsprechenden Werten, z.B. München 1600000 oder Hamburg 1800000.
Implementiert die __str__ Methode, sodass die Ausgabe der Instanz so aussieht:

name: Hamburg, population: 1800000

Zusatzaufgabe:
Erweitere die Klasse City um eine Methode compare_population, die
eine andere City-Instanz als Argument erhält und einen
Vergleich der Einwohnerzahl durchführt.

Die Methode soll folgenden Text zurückgeben:

    Wenn die aktuelle Stadt mehr Einwohner hat:
    "München hat eine höhere Einwohnerzahl als Hamburg."

    Wenn weniger:
    "Hamburg hat eine höhere Einwohnerzahl als München."

    Wenn gleich:
    "München und Hamburg haben die gleiche Einwohnerzahl."
"""

from __future__ import annotations

# from __future__ import annotations sorgt dafür, dass
# City als Typehint in der Klasse City genutzt werden kann


class City:
    def __init__(self, name: str, population: int) -> None:
        self.name = name
        self.population = population

    def __str__(self) -> str:
        # :, für Tausender-Trenner
        return f"name: {self.name}, population: {self.population:,}"

    def compare_population(self, city: City) -> str:
        """Vergleiche Population von self und city."""

        if not isinstance(city, City):
            raise TypeError("city muss vom Typ City sein!")

        if self.population > city.population:
            return f"{self.name} hat eine höhere Einwohnerzahl als {city.name}"
        elif self.population < city.population:
            return f"{city.name} hat eine höhere Einwohnerzahl als {self.name}"
        else:
            return f"{city.name} und {self.name} hat die gleiche Einwohnerzahl"


hamburg = City(name="Hamburg", population=16_384_783)
muenchen = City(name="München", population=6_384_783)
print(hamburg)

print(hamburg.compare_population(muenchen))
