class Konto:
    def zinsen_berechnen(self):
        raise NotImplementedError("Subclasses should implement this!")


class Sparkonto(Konto):
    def zinsen_berechnen(self):
        return "Zinsen für Sparkonto berechnet"


class Girokonto(Konto):
    def zinsen_berechnen(self):
        return "Zinsen für Girokonto berechnet"


konten = [Sparkonto(), Girokonto()]

for konto in konten:
    print(konto.zinsen_berechnen())
