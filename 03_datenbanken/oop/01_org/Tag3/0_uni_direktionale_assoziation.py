"""
Unidirektionale Assoziation

Eine Ausgangsklasse (Car) hat eine einseitige Assoziation
mit einer Zielklasse (Engine).
Die Zielklasse hat keine Kenntnis von der
Ausgangsklasse.


classDiagram
    class Engine {
        +name string
        +power int
        +start()
    }

    class Car {
        -engine: Engine
        +drive()
    }

    Car --> Engine : uses

"""


class Engine:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def start(self):
        print("Motor wird gestartet...")


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Auto fährt los")


engine = Engine("v8", 1200)
car = Car(engine)
car.drive()
