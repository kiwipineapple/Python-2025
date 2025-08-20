# In Python ist alles ein Objekt

x = 1  # 1, Objekt der Klasse Integer
print("Klasse von x:", type(x))  # <class 'int'>
y = int(42)


class House:
    """Der Docstring der Klasse House."""

    pass


house = House()  # Objekt (Instanz), der Klasse House
print(type(house))  # <class '__main__.House'>

small_house = House()
copy_house = small_house  # KOPIERT NUR REFERENZ!!!

# id() gibt die Identität (=Speicheradresse) des Objekts.
# Objekte mit selber Speicheradresse sind gleich (is-Operator)
print("id von house:", id(house))
print("id von small_house:", id(small_house))

# mit dem is-Operator prüfen, ob es das selbe Objekt ist:
print("is house small_house:", house is small_house)  # False
print("is house house:", house is house)  # True
print("is copy_house small_house:", copy_house is small_house)  # True

# Alle Attribute und Methoden
print(small_house.__dict__)  # eigene Klasse
print(dir(small_house))  # darüberhinaus vorhanden
