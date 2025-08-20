"""
Python prüft die except-Blöcke von oben nach unten, und sobald einer passt, wird nur dieser ausgeführt.
Danach werden keine weiteren except-Blöcke geprüft.

Viele Fehlertypen sind Unterklassen anderer Fehlerklassen.
Zum Beispiel:

LookupError
 ├── IndexError
 └── KeyError

Wenn du zuerst except LookupError: schreibst, fängt es auch IndexError und KeyError ab,
bevor Python diese speziellen Blöcke erreicht.
"""

try:
    liste = [1, 2]
    print(liste[5])  # IndexError
except LookupError:
    print("Genereller Suchfehler : ")  # Wird ausgeführt
except IndexError:
    print("Index war ungültig.")        # Wird NIE erreicht



"""
  Ziel: Wir möchten einen allgemeinen except-Block für alle Lookup-Fehler (z.B. KeyError, IndexError etc.),
          aber gleichzeitig auch einen spezifischen Block für IndexError – denn für diesen Fall haben wir 
           eine gezielte Behandlung vorgesehen.

 ️ Problem: Da IndexError eine Unterklasse von LookupError ist, wird bei einem IndexError
             bereits der allgemeine LookupError-Block ausgeführt – **bevor** Python den spezifischen 
              IndexError-Block erreicht.

  Deshalb wird unser spezieller Code für IndexError **nicht ausgeführt**, obwohl er im Code steht.
  Die Reihenfolge der except-Blöcke ist entscheidend: **erst spezifisch, dann allgemein.**


"""