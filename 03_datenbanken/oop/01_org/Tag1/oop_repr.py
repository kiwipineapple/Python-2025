"""
Implementieren der String-Repräsentation: __repr__
gesprochen: dunder-Repr

__repr__ ist die interne String-Repräsentation für Debugging und Entwickler-Zwecke.
"""

import matplotlib.pyplot as plt
from pprint import pprint
import random


class DataPoint:
    """Ein einfacher Datenpunkt mit x und y Koordinate."""

    def __init__(self, name: str, x: float, y: float):
        """
        Args:
            name: Name des Datenpunktes
            x: X-Koordinate
            y: X-Koordinate
        """
        self.name = name
        self.x = x
        self.y = y

    def scale(self, factor: float) -> None:
        """
        Skaliert x und y- Koordinate des Datenpunkts.

        Args:
            factor: Skalierungsfaktor
        """
        self.x *= factor
        self.y *= factor

    def __str__(self) -> str:
        return f"{self.name}, {self.x} / {self.y}"

    def __repr__(self) -> str:
        return f"DataPoint('{self.name}', {self.x}, {self.y})"


p1 = DataPoint("P1", 2.3, 3.2)
p1.scale(2)
print(p1)


def plot_datapoints(data_points: list[DataPoint]) -> None:
    """
    Scatterplot von DataPoint-Objekten.

    Args:
        data_points: Liste von Datenpunkten
    """
    x = [dp.x for dp in data_points]  # x-werte aus Datapoints extrahieren
    y = [dp.y for dp in data_points]  # y-werte aus Datapoints extrahieren

    plt.scatter(x, y)
    plt.show()


def generate_datapoints(n: int) -> list[DataPoint]:
    data_points: list[DataPoint] = []
    for i in range(n):
        name = f"P{i}"
        x = random.uniform(-100, 100)  # aus Gleichverteilung, random.uniform()
        y = random.uniform(-100, 100)
        dp = DataPoint(name, x, y)
        data_points.append(dp)
    return data_points


data_points = generate_datapoints(n=100)  # [DataPoint(..), DataPoint(...)]
plot_datapoints(data_points)
