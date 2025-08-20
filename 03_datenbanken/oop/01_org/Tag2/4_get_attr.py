"""
getattr,
setattr,
delattr
"""


class BananaTree:

    anzahl = 0

    def __init__(self, bananas: int):
        self.bananas = bananas
        BananaTree.anzahl += 1

    def __str__(self) -> str:
        return f"Bananenbaum mit {self.bananas} Bananen"

    def __repr__(self) -> str:
        # via self.__class__.__name__ den Namen der Klasse ermitteln
        return f"{self.__class__.__name__}(bananas={self.bananas})"

    def say(self):
        pass


tree = BananaTree(190)
print("Repräsentation von Bananatree:", repr(tree))  # BananaTree(bananas=190)

tree2 = BananaTree(190)

tree.bananas  # lesender Zugriff
tree.bananas = 100
# tree.rotten_bananas = 3  # neues Attribut rotten_bananas
# del tree.bananas

# lesender dynamischer Zugriff auf tree.bananas
print(getattr(tree, "bananas"))

# schreibenden dynamischer Zugriff auf tree.bananas
setattr(tree, "bananas", 42)  # tree.bananas = 42
print("Anzahl bananas:", tree.bananas)

# löschender Zugriff auf tree.bananas
# delattr(tree, "bananas")
# print(getattr(tree, "bananas"))  # AttributeError
# setattr(tree, "orangen", 142)

# print(BananaTree.trees)

print(getattr(BananaTree, "anzahl"))  # 2

# AttributError. BananaTree hat kein Attribut bananas
# print(getattr(BananaTree, "bananas")) AttributeError!!!!

# Zugriff auf Methode say() BananaTree
getattr(BananaTree, "say")  # funktioniert

# Zugriff auf Methode say() des Tree-Objekts
getattr(tree, "say")  # tree.say(), funktioniert

print(tree.__dict__)  # alle Attribute eines Objekts
print(vars(tree))  # alle Attribute eines Objekts
print(dir(tree))
