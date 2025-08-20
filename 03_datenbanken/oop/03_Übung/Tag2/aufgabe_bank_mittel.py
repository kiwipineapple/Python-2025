"""(MITTEL)
Erstelle eine Klasse Konto mit den Methoden
1) withdraw (Abbuchen)
2) deposit (Einzahlen)
3) __str__ (Liefert Kontostand in Euro)

4) und einem Attribut balance (Kontostand in Cent) als getter und setter.
5) Zur Validierung der Eingabe soll eine Methode validate(value) erstellt werden.
Diese kann in den Methoden withdraw und deposit aufgerufen werden.

Erstelle zwei Konto-Instanzen und überweise Geld von einem Konto auf das
andere. Ein Konto darf nicht überzogen werden (< 0 Euro).
Einheiten werden im Finanzbereich häufig in Cent-Beträgen angegeben (Datentyp int).

Beispiel:
konto_1 = Konto(initial=10_000, name="Bob")
konto_2 = Konto(initial=1200, name="Alice")
print(konto_2)

>> Auf dem Konto befinden sich zur Zeit 12.00 Euro

# Validierung der Eingabe
amount = konto_1.withdraw(amount="abc")
>> Dieser Vorgang ist nicht möglich! Es können nur ganzzahlige Werte übergeben werden.

# Überweisung von Konto 1 auf Konto 2
amount = konto_1.withdraw(amount=100)
konto_2.deposit(amount=amount)

# Zusatz-Überlegungen
Was ist bei diesem Vorgehen problematisch?

"""


class Konto:
    def __init__(self, initial: int, name: str) -> None:
        self.balance = initial

    def __str__(self) -> str:
        return f'Auf dem Konto befinden sich zur Zeit {self.balance / 100} Euro'
    ############################## Error#####################
    # @property
    # def withdraw(self):
    #     return self._amount

    # @withdraw.setter
    # def withdraw(self, amount: int):
    #     if amount > self.balance:
    #         raise ValueError('Ein Konto darf nicht überzogen werden')
    #     elif type(amount) != int:
    #         raise TypeError(
    #             'Dieser Vorgang ist nicht möglich! Es können nur ganzzahlige Werte übergeben werden.')
    #     self._amount = amount

    # @property
    # def deposit(self):
    #     return self.balance

    # @deposit.setter
    # def deposit(self, amount: int):
    #     if amount > self.balance:
    #         raise ValueError('Ein Konto darf nicht überzogen werden')
    #     self.balance -= amount

    # def validate(self, value):
    #     self.balance -= value
    ###########################################################
    def validate(self, amount):
        if not isinstance(amount, int):
            raise TypeError(
                'Es können nur ganzzahlige Werte übergeben werden.')
        if amount < 0:
            raise ValueError('Es können nur positve Werte übergeben werden.')

    @property
    def balance(self) -> int:
        return self._balance

    @balance.setter
    def balance(self, value: int) -> None:
        self._balance = value

    def withdraw(self, amount: int) -> int:
        self.validate(amount)
        if self._balance > amount:
            self._balance -= amount
        else:
            raise ValueError('Ein Konto darf nicht überzogen werden')
        return amount

    def deposit(self, amount: int) -> None:
        self.validate(amount)
        self._balance += amount


def main():
    konto_1 = Konto(initial=10000, name="Bob")
    konto_2 = Konto(initial=1200, name="Alice")
    print(konto_1)

    try:
        amount = konto_2.withdraw('abc')
        konto_1.deposit(amount)
    except Exception as e:
        print('Fehler in Überweisung: ', e)


main()
