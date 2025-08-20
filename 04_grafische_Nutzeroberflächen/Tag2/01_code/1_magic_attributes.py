class Auto:
    """
    Eine einfache Klasse, die ein Auto repräsentiert. Sie speichert Informationen über das Modell,
    die Marke und das Herstellungsjahr des Autos.
    """

    def __init__(self, marke, modell, jahr):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr


# Eine Instanz von Auto erstellen
mein_auto = Auto("Toyota", "Corolla", 2021)

# Verwendung von magischen Attributen
# print("Dokumentation der Auto-Klasse:", Auto.__doc__)
# print("Wörterbuch der Auto-Instanz:", mein_auto.__dict__)
print("Klass :", mein_auto.__class__)
# print("Klassenname :", mein_auto.__class__.__name__)
# print("Class Module:", Auto.__module__)
print("Class Elternklassen:", Auto.__bases__)
