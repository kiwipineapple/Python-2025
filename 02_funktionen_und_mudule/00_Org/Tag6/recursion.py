def fakultaet(n):
    if n == 0:
        return 1
    return n * fakultaet(n - 1)


print(fakultaet(5))  # Ausgabe: 120

print(fakultaet(0))  # 1
print(fakultaet(1))  # 1 * ergebnis von  fakultaet(1-1) = 1
print(fakultaet(2))  # 2 * ergebnis von  fakultaet(1) = 2
print(fakultaet(3))  #
print(fakultaet(4))  #
print(fakultaet(5))  # 5 * ergebnis von  fakultaet(5-1) = 2



#  Elegant und mathematisch direkt, aber potenziell speicherintensiver (Tiefenaufrufe im Callstack)



def fakultaet_iterativ(n):
    ergebnis = 1
    for i in range(1, n + 1):
        ergebnis *= i
    return ergebnis

# print(fakultaet_iterativ(5))
# Stabil und effizient – auch bei größeren Zahlen oft besser geeignet



"""
Rekursion besteht immer aus zwei Phasen:

VORWÄRTS-Phase (Aufbau der Aufrufe) :
    -> In dieser Phase zählt oder berechnet die Funktion noch nichts. Wird noch nicht multipliziert
    -> Sie ruft sich einfach immer weiter selbst auf, mit einem jeweils „kleineren“ Parameter (z.B. n-1 oder text[1:]).
    -> Dabei 'merkt' sich Python jede einzelne Funktionsaufruf-Stufe im Speicher (Call-Stack), z.B.:
                
        fakultaet(5)
         → 5 * fakultaet(4)
               → 4 * fakultaet(3)
                     → 3 * fakultaet(2)
                           → 2 * fakultaet(1)
                                 → 1 * fakultaet(0)
                                       → fakultaet(0) = 1  ← Abbruchbedingung!

        Python merkt sich nur: → „Ich muss später 1 * …, dann 2 * …, dann 3 * … usw. berechnen“
        Noch keine Ergebnisse oder Rückgaben!!!
 
RÜCKWÄRTS-Phase (ab jetzt wird gerechnet!)
    -> Sobald die Abbruchbedingung erfüllt ist, kehrt jede Funktion eine Ebene zurück.
    -> Dann beginnt die eigentliche Berechnung 
    -> Die Funktionen lösen sich schrittweise wieder auf – von unten nach oben.
 
        fakultaet(0) = 1                         # Abbruchbedingung: Rückgabe 1

        → fakultaet(1) = 1 * 1 = 1               # 1 kommt von fakultaet(0)
        
        → fakultaet(2) = 2 * 1 = 2               # 1 kommt von fakultaet(1)
        
        → fakultaet(3) = 3 * 2 = 6               # 2 kommt von fakultaet(2)
        
        → fakultaet(4) = 4 * 6 = 24              # 6 kommt von fakultaet(3)
        
        → fakultaet(5) = 5 * 24 = 120            # 24 kommt von fakultaet(4)


 
"""



"""
Rekursion ist nicht immer die effizienteste, aber oft die klarste Lösung.
Besonders bei verschachtelten oder „sich wiederholenden“ Strukturen.

Wenn die Tiefe des Problems nicht vorhersehbar ist (z.B. bei Dateien in Unterordnern), 
ist Rekursion viel flexibler als Schleifen.

Viele Algorithmen sind rekursiv definiert
Z.B.:

Fibonacci-Zahlen

Suchalgorithmen in Bäumen (DFS)

Traversieren von XML/HTML/JSON

Backtracking (Sudoku, Labyrinth, Schachprobleme)
"""