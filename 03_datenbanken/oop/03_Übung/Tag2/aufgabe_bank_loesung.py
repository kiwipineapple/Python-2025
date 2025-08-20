"""
Problem: falls eine Abbuchung vorgenommen wird und die Überweisung fehlschlägt,
stimmen die Konten nicht mehr.

Die Lösung wäre ein Rollback-Verfahren oder Datenbank-Tranksaktionen (SQL).
"""


class Konto:
    def __init__(self, initial: int, name: str) -> None:
        self.name = name
        self.balance = initial

    def validate(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Nur ganzzahlige Beträge sind erlaubt.")
        if value < 0:
            raise ValueError("Betrag darf nicht negativ sein.")

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, value: int) -> None:
        self.validate(value)
        self._balance = value

    def __str__(self) -> str:
        return f"{self.name}: {self.balance / 100:.2f} €"

    def withdraw(self, amount: int) -> int:
        self.validate(amount)
        if amount > self._balance:
            raise ValueError("Nicht genügend Guthaben.")
        self._balance -= amount
        return amount

    def deposit(self, amount: int) -> None:
        self.validate(amount)
        self._balance += amount


# Beispiel
konto_1 = Konto(initial=10_000, name="Bob")
konto_2 = Konto(initial=1200, name="Alice")

try:
    betrag = konto_1.withdraw(10_000)
    konto_2.deposit(betrag)
except Exception as e:
    print("Fehler bei der Überweisung:", e)

print(konto_1)
print(konto_2)

