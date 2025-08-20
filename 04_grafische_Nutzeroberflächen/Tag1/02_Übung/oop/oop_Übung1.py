class Instrument:
    def __init__(self, name: str, typ: str) -> None:
        self.name = name
        self.typ = typ

    def spiele(self) -> None:
        print(f'Die {self.name}, ein {self.typ} spielt ein ruhiges Lied.')


obj1 = Instrument(name='Klavier', typ='Tasteninstrument')
obj1.spiele()
