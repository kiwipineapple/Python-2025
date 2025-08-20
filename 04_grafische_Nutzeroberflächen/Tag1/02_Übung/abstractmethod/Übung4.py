from abc import ABC, abstractmethod


class Zahlung(ABC):
    @abstractmethod
    def starte_zahlung(self, betrag):
        pass

    @abstractmethod
    def prüfe_zahlung(self):
        pass


class Kreditkartenzahlung(Zahlung):
    def starte_zahlung(self, betrag):
        return f'Mit Kreditkarte {betrag}€ zahlen.'

    def prüfe_zahlung(self):
        return f'Mit Kreditkarte zahlen prüfen.'


class Paypalzahlung(Zahlung):
    def starte_zahlung(self, betrag):
        return f'Mit Paypal {betrag}€ zahlen.'

    def prüfe_zahlung(self):
        return f'Mit Paypal zahlen prüfen.'


karte = Kreditkartenzahlung()
print(karte.starte_zahlung(50))
print(karte.prüfe_zahlung())

paypal = Paypalzahlung()
print(paypal.starte_zahlung(80))
