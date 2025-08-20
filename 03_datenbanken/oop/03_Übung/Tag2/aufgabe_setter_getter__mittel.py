"""
Vervollständige die Klasse Produkt und lege die entsprechenden Properties an. (MITTEL)

# Es gelten folgende Constraints (Regeln):
- Der Preis darf nicht negativ sein und muss eine Zahl sein
- Die Verfügbarkeit muss den Zustand "in stock" oder "out of stock" haben.
- Im Fehlerfall raise ValueError.

Implementiere auch __str__ und __repr__.

Teste mit folgenden Produkten:
products = [
    ("Maggi", 23.2, "in stock"),
    ("Snickers", 4, "out of stock"),
    ("Petersilie", 1.9, "stock"),  # muss scheitern, da "stock" kein gültiger Zustand ist
    ("Gouda Käse", -12.50, "out of stock"), # muss scheitern, da Preis negativ ist
    ("Shampoo", 23.2, "inn stock"),  # muss scheitern, da "inn stock" kein gültiger Zustand ist
]
Nutze zum testen einen Loop und try-except
"""


class Produkt:
    def __init__(self, name, preis, verfuegbarkeit):
        # Hier müssen die Instanzvariablen initialisiert werden
        self.name = name
        self.preis = preis
        self.verfuegbarkeit = verfuegbarkeit

    # Getter-Methode für preis

    # Getter-Methode für verfuegbarkeit

    # Setter-Methode für preis

    # Setter-Methode für verfuegbarkeit


if __name__ == "__main__":
    products = [
        ("Maggi", 23.2, "in stock"),
        ("Snickers", 4, "out of stock"),
        ("Petersilie", 1.9, "stock"),  # muss scheitern
        ("Gouda Käse", -12.50, "out of stock"),  # muss scheitern
        ("Shampoo", 23.2, "inn stock"),  # muss scheitern.
    ]

    for product in products:
        try:
            Produkt(...)
        except ValueError as e:
            print(f"es ist ein Fehler aufgetreten: {e}")
