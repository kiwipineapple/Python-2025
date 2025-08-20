class SmartDevice:
    def __init__(self, name, status) -> None:
        self.name = name
        self.status = status

    def zeige_status(self):
        print(f"{self.name} ist {self.status}.")


class SmartLampe(SmartDevice):
    def __init__(self, name, status, helligkeit) -> None:
        super().__init__(name, status)
        self.helligkeit = helligkeit

    def zeige_helligkeit(self):
        print(f"{self.name} ist {self.status}, Helligkeit ist {self.helligkeit}%.")


smartlampe = SmartLampe('lampe', 'an', 70)
smartlampe.zeige_helligkeit()
