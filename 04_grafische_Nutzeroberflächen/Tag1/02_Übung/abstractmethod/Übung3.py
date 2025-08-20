from abc import ABC, abstractmethod


class Fahrzeug(ABC):
    @abstractmethod
    def starte_motor(self):
        pass

    @abstractmethod
    def stoppe_motor(self):
        pass


class Auto(Fahrzeug):
    def __init__(self) -> None:
        self.n = 0

    def starte_motor(self):
        self.n += 1
        return f'{self.n} Motors sind gestartet.'

    def stoppe_motor(self):
        self.n -= 1
        return f'{self.n} Motors läuft.'


motors = Auto()
motors.starte_motor()
motors.starte_motor()
f = motors.starte_motor()
print(f)
f = motors.stoppe_motor()
print(f)
