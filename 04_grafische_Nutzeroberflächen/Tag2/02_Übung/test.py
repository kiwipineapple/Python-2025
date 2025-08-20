class Benutzer:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'Benutzer ist {self.name}'

    def __repr__(self) -> str:
        return f'Benutzer: {self.name!r}'


q = Benutzer('Alice')
print(repr(q))

print(q.__dict__)
