"""
Enumerationen

"in stock", "out of stock"

Eigenschaften eines Enums:
Can't be instantiated
Can't be subclassed unless the base enum has no members
Provide a human-readable string representation for their members
Are iterable, returning their members in a sequence
Provide hashable members that can be used as dictionary keys
Support the square bracket syntax, call syntax, and dot notation to access members
Don’t allow member reassignments
"""

import enum


class Day(enum.StrEnum):
    SUN = "Sonntag"
    MON = "Montag"


class Availability(enum.StrEnum):
    IN_STOCK = "in stock"
    OUT_OF_STOCK = "out of stock"


print("Sonntag:", Day.SUN)


class Product:
    def __init__(self, name, verfuegbarkeit: Availability):
        self.verfuegbarkeit = verfuegbarkeit


p = Product("Käse", Availability.IN_STOCK)
p.verfuegbarkeit = Availability.OUT_OF_STOCK


if p.verfuegbarkeit == Availability.OUT_OF_STOCK:
    print("Produkt ist nicht mehr verfügbar")


# über das Enum Day iterieren
for day in Day:
    print("=>", day)

if p.verfuegbarkeit in Availability:
    print("out of stock ist im Enum Availability")

if p.verfuegbarkeit in Availability:
    print("out of stock ist im Enum Availability")
