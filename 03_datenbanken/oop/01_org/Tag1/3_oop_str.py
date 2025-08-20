"""
Implementieren der String-Repräsentation: __str__
gesprochen: dunder-String (dunder=double under)

__str__ ist die String-Repräsentation für den Endnutzer. Sie sollte
benutzerfreundlich dargestellt sein.
"""


class Person:
    """Beschreibt eine Person."""

    def __init__(self, name: str, age: int) -> None:
        """Konstruktor (Initialisierer)"""
        print("id von self:", id(self))
        self.name = name
        self.age = age
        self.hobbies = []

    def introduce(self) -> None:
        print(f"Hallo, ich bin {self.name} und bin {self.age} Jahre alt.")

    def __str__(self) -> str:
        """Diese Methode MUSS einen String zurückgeben."""
        return f"{self.name}: {self.age}"


bob = Person(name="Bob", age=42)  # Instanziieren
alice = Person(name="Alice", age=32)

# Aufrufen der String-Repräsentation via print() oder str()
print(bob)
