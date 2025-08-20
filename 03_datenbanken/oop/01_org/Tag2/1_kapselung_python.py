"""
Getter und Setter in Python

Getter ist eine Zugriffsmethoden.
Setter ist eine Änderungsmethode.

Constraints:
Regeln des Datenmodels
"""


class Person:
    def __init__(self, name: str, age: int):
        self.name = name  # ruft name.setter auf
        self.age = age

    @property
    def name(self):
        """Getter des Attributs name."""
        return self._name

    @name.setter
    def name(self, new_name: str):
        """Setter des Attributes name."""
        if len(new_name) < 3:
            raise ValueError("Name ist zu kurz")

        self._name = new_name


p = Person("Alice", 34)
p.name = "Bob"  # öffentliches Interface, ruft name.setter auf
p.name  # ruft property name auf (getter)
p.age = 343  # Setzt Wert von age direkt (ohne setter)
