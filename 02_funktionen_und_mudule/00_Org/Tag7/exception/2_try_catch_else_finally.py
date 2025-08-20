"""

# Ohne Fehlerbehandlung (nicht empfohlen):
# Wenn die Datei nicht existiert, stürzt das Programm ab.
data = open('meaw_datei.txt', 'r')
content = data.read()

"""

# Mit Fehlerbehandlung: sicheres Öffnen der Datei
try:
    # Versuche die Datei zu öffnen (Dateinamen hier anpassen)
    datei = open('meine_datei.txt', 'r') #  ändere diesen Namen für Tests
    inhalt = datei.read()
except FileNotFoundError:
    # Wird ausgeführt, wenn die Datei nicht gefunden wird
    print("Die Datei wurde nicht gefunden.")
else:
    # Wird nur ausgeführt, wenn kein Fehler im try-Block aufgetreten ist
    print("Dateiinhalt:", inhalt)
finally:
    # Wird immer ausgeführt – egal ob Fehler oder nicht
    print("In Finally Block - Datei Schließen")

"""



"""

# TODO : Ändere den Dateinamen oben mehrfach: einmal mit existierender Datei (z.B. 'datei.txt')
#  - einmal mit falschem Dateinamen (z.B. 'falsch.txt')
#  Führe den Code nach jeder Änderung aus
#  ➜ Beobachte, wann welcher Block (except, else, finally) ausgeführt wird



"""
Der finally-Block ist besonders nützlich, wenn Sie sicherstellen möchten, dass bestimmte 
Bereinigungsaktionen immer durchgeführt werden, egal ob eine Exception aufgetreten ist oder nicht.
 
 Typische Anwendungsfälle sind das Schließen von Dateien oder das Freigeben von Ressourcen, 
 wie Datenbankverbindungen.

"""