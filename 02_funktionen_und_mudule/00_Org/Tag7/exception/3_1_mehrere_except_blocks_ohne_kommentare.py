try:
    zahl = int(input("Bitte eine Zahl eingeben: "))
    ergebnis = 10 / zahl
    beispiel_liste = [10, 20, 30]
    print(beispiel_liste[2])
except ValueError:
    print("Ungültige Eingabe – bitte eine Zahl eingeben.")
except ZeroDivisionError:
    print("Division durch Null ist nicht erlaubt.")
except NameError:
    print("Schau nochmal, ob deine Variable definiert ist.")
except IndexError:
    print("Deine Liste ist kleiner als du denkst (Index zu groß).")
except (TypeError, KeyError) as e:
    print("Fehler aufgetreten :", type(e).__name__, "-", e)
else:
    print("Ergebnis:", ergebnis)
finally:
    print("Berechnung abgeschlossen.")






"""
#    Führe den Code im try-Block absichtlich mit verschiedenen Fehlern aus,
#    um zu beobachten, welcher except-Block jeweils aktiviert wird.
#    So lernst du, wie Python auf unterschiedliche Fehlertypen reagiert.
   
    # Uncomment für TypeError:
    # len(zahl) → zahl ist int, aber len() erwartet eine Sequenz wie String oder Liste
    #print("Länge der Zahl:", len(zahl))

    # Uncomment für KeyError:
    # Zugriff auf einen nicht vorhandenen Schlüssel im Dictionary
    # beispiel_dict = {"a": 1, "b": 2}
    # print(beispiel_dict["c"])

    # Uncomment für NameError:
    # print("Der Wert ist:", lol)  # Variable lol wurde nie definiert

    # Uncomment für IndexError:
    # beispiel_liste = [10, 20, 30]
    # print(beispiel_liste[5])  # Liste hat keinen Index 5

"""