"""
Hallo
"""

x = 100  # global

def outer():
    """outer funktion
    """
    x = 50  # enclosing
    def inner():
        x = 10  # local
        print(x)
    inner()
outer()

for x in range(10):
    print(x)

"""
Namensraum = Bereich, in dem ein Name (z. B. Variable) gültig ist.

LEGB-Regel: Reihenfolge bei Namensauflösung:

Local: innerhalb der aktuellen Funktion

Enclosing: umgebende Funktion (bei verschachtelten Funktionen)

Global: auf Modulebene

Built-in: Python-Standardnamen
"""


#zahl = [1, 2, 3]
#print(len(zahl))

# Built-in-Funktion len() → Ausgabe: 3
# len ist nicht lokal, nicht global, nicht enclosing – aber Python kennt len() als eingebaute Funktion,
# weil sie Teil des Built-in-Namensraums ist.

#Zeige mit globals() und locals() an, was gerade im jeweiligen Namensraum enthalten ist:

# print(globals().keys())
# print(locals().keys())

def test():
    m = 123
    print("GLOBALS:", globals().keys())
    print("LOCALS:", locals().keys())

test()

"""
def test():
    m = 123
    print("GLOBALS:", globals().keys())
    print("LOCALS:", locals().keys())

test()

globals() zeigt weiterhin nur das, was außerhalb der Funktion definiert wurde.

locals() zeigt nur, was in der Funktion test() definiert ist → z.B. x.
"""

# print(__name__)  #was kommt ?
print(__doc__)
print(outer.__doc__)

# Vermeide es, eingebaute Funktionsnamen wie print, list, len, input, sum usw. als eigene Variablennamen zu verwenden.
# → Sie funktionieren zwar technisch, aber überschreiben die ursprüngliche Funktion und führen leicht zu Fehlern.
# Du kannst dir die eingebauten Namen so anzeigen lassen:
import builtins
print(dir(builtins))
