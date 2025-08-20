"""
Getter und Setter in der klassischen OOP.
In Python wird es anders gemacht.

Getter ist eine Zugriffsmethoden.
Setter ist eine Änderungsmethode.

Constraints:
Regeln des Datenmodels
"""


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def set_name(self, new_name: str):
        if len(new_name) < 3:
            raise ValueError("Name ist zu kurz")

        self.name = new_name

    def get_name(self) -> str:
        return self.name


person = Person("Bob", 42)
# person.name = [3, 2, 2]
# print(person.name)
person.set_name("Bo")  # Ändern des Attributs Name
person.get_name()  # Zugriff auf das Attribut Name
