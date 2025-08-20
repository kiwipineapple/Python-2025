"""
Wichtig zur Reihenfolge von except-Blöcken:

- Python prüft die except-Blöcke von oben nach unten.
  Sobald ein Block auf den Fehler passt, wird **nur dieser eine** ausgeführt.

- Ein Tupel wie (TypeError, KeyError) fängt **mehrere Fehlerarten** auf einmal ab.
  Wenn es zu früh steht, fängt es auch Fehler wie KeyError ab – noch **bevor** ein spezifischer Block erreicht wird.

Deshalb: Immer **spezifische Fehler zuerst**, dann allgemeine oder kombinierte except-Blöcke.
"""

# ❌ Falsche Reihenfolge – der spezifische Block wird übersprungen

try:
    my_dict = {"a": 1}
    print(my_dict["b"])  # KeyError
except (TypeError, KeyError):
    print("Allgemeiner Fehler (Type oder Key).")
except KeyError:
    print("Spezifischer KeyError.")




# ✅ Richtige Reihenfolge – der spezifische Block wird erreicht
try:
    my_dict = {"a": 1}
    print(my_dict["b"])  # KeyError
except KeyError:
    print("Spezifischer KeyError.")        # <-- Wird ausgeführt
except (TypeError, KeyError):
    print("Allgemeiner Fehler (Type oder Key).")
