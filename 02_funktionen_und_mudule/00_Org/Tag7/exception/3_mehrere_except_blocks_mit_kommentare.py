try:
    # Benutzer gibt eine Zahl ein (als String) – wird mit int() umgewandelt
    zahl = int(input("Bitte eine Zahl eingeben: "))

    # Berechnung – kann ZeroDivisionError verursachen, wenn zahl == 0
    ergebnis = 10 / zahl

    # Uncomment für TypeError:
    # len(zahl) → zahl ist int, aber len() erwartet eine Sequenz wie String oder Liste
    #print("Länge der Zahl:", len(zahl))

    # Uncomment für KeyError:
    # Zugriff auf einen nicht vorhandenen Schlüssel im Dictionary
    beispiel_dict = {"a": 1, "b": 2}
    print(beispiel_dict["c"])

    # Uncomment für NameError:
    # print("Der Wert ist:", lol)  # Variable lol wurde nie definiert

    # Uncomment für IndexError:
    # beispiel_liste = [10, 20, 30]
    # print(beispiel_liste[5])  # Liste hat keinen Index 5

except ValueError:
    # Wird ausgelöst, wenn input kein gültiger int ist (z.B. "abc")
    print("Ungültige Eingabe – bitte eine Zahl eingeben.")
except ZeroDivisionError:
    # Tritt auf, wenn der Benutzer 0 eingibt → Division durch 0
    print("Division durch Null ist nicht erlaubt.")
except NameError:
    # Fehler, wenn eine Variable verwendet wird, die nicht definiert ist
    print("Schau nochmal, ob deine Variable definiert ist.")
except IndexError:
    # Zugriff auf einen ungültigen Index in einer Liste
    print("Deine Liste ist kleiner als du denkst (Index zu groß).")
except (TypeError, KeyError) as e:
    # Gruppierte Fehlerbehandlung:
    # TypeError: falscher Typ, z.B. len(zahl)
    # KeyError: Schlüssel nicht im Dictionary vorhanden

    # 'e' ist das Fehlerobjekt, das beim Auftreten der Exception erzeugt wird.
    # Es enthält alle Informationen über den Fehler.
    # - 'type(e).__name__' gibt den Namen der Fehlerklasse zurück (z.B. 'KeyError').
    # - 'e' alleine gibt die Standard-Fehlermeldung aus (z.B. den fehlenden Schlüssel).

    # Das Schlüsselwort 'as' wird verwendet, um einem Objekt einen Namen (Alias) zu geben
    # – zum Beispiel dem Fehlerobjekt in einem except, einer Datei im with-Block oder einem
    # Modul beim Import.

    print("Fehler aufgetreten :", type(e).__name__, "-", e)
else:
    # Wird nur ausgeführt, wenn im try-Block kein Fehler aufgetreten ist
    print("Ergebnis:", ergebnis)
finally:
    # Wird immer ausgeführt – egal ob Fehler oder nicht
    print("Berechnung abgeschlossen.")
