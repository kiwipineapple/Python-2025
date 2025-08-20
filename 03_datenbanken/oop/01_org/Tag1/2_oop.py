"""
Erstellen einer ersten Klasse Person
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


bob = Person(name="Bob", age=42)  # Instanziieren
alice = Person(name="Alice", age=32)

print("id von p1:", id(bob))
print("is instance:", isinstance(bob, Person))
print("type:", type(bob) == Person)
# alice.city = "Hamburg"  BAD PRACTISE

print(bob.__dict__)
print(alice.__dict__)

bob.introduce()
print(bob)
print(alice)


# Würde Fehler ergeben, da bob kein city-Attribut
# for person in [alice, bob]:
#     print(person.city)
