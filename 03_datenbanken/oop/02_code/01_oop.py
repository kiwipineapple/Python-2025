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

print(bob.age)