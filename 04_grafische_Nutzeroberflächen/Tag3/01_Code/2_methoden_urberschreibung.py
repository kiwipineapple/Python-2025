class Essen:
    def geschmack(self):
        return "Dieses Essen hat einen allgemeinen Geschmack."


class Pizza(Essen):
    def geschmack(self):
        return "Diese Pizza schmeckt würzig und käsig."


class Eis(Essen):
    def geschmack(self):
        return "Dieses Eis schmeckt süß und cremig."


class Kaffee(Essen):
    def geschmack(self):
        return "Dieser Kaffee schmeckt bitter und aromatisch."


# Liste von verschiedenen Essensobjekten
essen_liste = [Pizza(), Eis(), Kaffee()]

# Iteration durch die Essensliste und Ausgabe des Geschmacks
for meaw in essen_liste:
    print(meaw.geschmack())
