"""
importlib erlaubt das dynamische Importieren von Modulen – nützlich bei:

flexiblen Tools

Plugins

Benutzereingaben
"""

import importlib

modulname = "math"
modulname1 = "random"

math_modul = importlib.import_module(modulname) # Du kannst zur Laufzeit Module laden, deren Name als Text vorliegt.
random_modul = importlib.import_module(modulname1)

print(math_modul.sqrt(25))  # Ausgabe: 5.0