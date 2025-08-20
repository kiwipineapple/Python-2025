class Datei:
    def __init__(self):
        print('init method')

    def __enter__(self):
        # Diese Methode wird aufgerufen, wenn der with-Block beginnt.
        # Hier kann z.B. eine Datei geöffnet, eine Verbindung hergestellt oder ein Lock gesetzt werden.
        print("Datei geöffnet")
        return self  # Gibt ein Objekt zurück, das im with-Block als 'as'-Variable verfügbar ist

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Diese Methode wird automatisch aufgerufen, wenn der with-Block endet – auch bei einem Fehler.
        print("Datei geschlossen")
        pass
        # return True
        # Wenn du True zurückgibst, wird die Ausnahme unterdrückt (nicht weitergegeben)


# Anwendung eines Kontextmanagers:
with Datei() as d:
    print("Datei wird benutzt")
    # print(1/0)
    # Hier könntest du absichtlich einen Fehler einbauen, z.B. 1 / 0,
    # um zu sehen, dass __exit__ trotzdem ausgeführt wird









"""
# Ein Kontextmanager ist eine Klasse, die mit 'with' verwendet werden kann.
# Er sorgt dafür, dass bestimmte Aktionen automatisch beim Start und Ende eines Blocks passieren.
# Dafür müssen die Methoden __enter__ (Start) und __exit__ (Ende) definiert sein.

# Typische Anwendungsfälle sind das Öffnen und automatische Schließen von Dateien, Verbindungen oder Ressourcen.

"""

"""
 def __exit__(self, exc_type, exc_val, exc_tb): ->

        # Die drei Parameter liefern Informationen über eine Ausnahme, falls im Block etwas schiefgeht:
        # exc_type:   exception type- Der Typ des Fehlers (z.B. ZeroDivisionError, FileNotFoundError)
        # exc_val:     Das konkrete Fehlerobjekt mit Nachricht
        # exc_tb:      Das Traceback-Objekt (enthält Infos, wo genau der Fehler passiert ist)

        # Wenn du True zurückgibst, wird die Ausnahme unterdrückt (nicht weitergegeben)
        # Wenn du None oder False zurückgibst, wird der Fehler normal ausgelöst (Standardverhalten)

        # Beispiel: return True → unterdrückt den Fehler (nicht empfohlen ohne guten Grund)
        # Hier: kein return → Fehler wird nicht unterdrückt
"""
