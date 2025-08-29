"""
Die Repräsentation von Python-Datentypen in einem f-String aufrufen

f"{x!r}" gibt die String-Repräsentation von Objekt x
"""

animals = ["cat", "dog"]
print(repr(animals))
print(str(animals))

print(f"{animals!r}")


class City:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r})"


hamburg = City("Hamburg")
print(repr(hamburg))  # City('Hamburg')
