
"""
Verwendung von `match` in Python (ab Version 3.10)

Die `match`-Anweisung ist vergleichbar mit `switch-case` aus anderen Programmiersprachen.
Sie wird verwendet, um Werte mit verschiedenen Fällen zu vergleichen.

Syntax:
---------
match variable:
    case Wert1:
        ...
    case Wert2:
        ...
    case _:
        ... (Standardfall)
"""

#  Beispiel 1: Einfache Befehlsauswertung
command = input("Gib einen Befehl ein (start, stop, hilfe, exit): ")

match command:
    
    case "start":
        print("System wird gestartet...")
    case "stop":
        print("System wird gestoppt...")
    case "hilfe":
        print("Verfügbare Befehle: start, stop, hilfe, exit")
    case "exit":
        print("Programm wird beendet.")
    case _:
        print("Unbekannter Befehl!")

#case _: ist der Standardfall (entspricht else bzw. default).

#  Beispiel 2: Match mit mehreren Werten (Pattern Matching)
status_code = 401

match status_code:
    case 200:
        print("OK")
    case 400 | 401 | 403:
        print("Clientfehler")
    case 404:
        print("Seite nicht gefunden")
    case 500:
        print("Serverfehler")
    case _:
        print("Unbekannter Statuscode")
