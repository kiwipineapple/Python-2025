class Beispiel:
    def __init__(self):
        print("in constructor enter")
        self.name = "Python"
        print("in constructor exit")

    def __getattr__(self, attr):
        # Wird aufgerufen, wenn das Attribut nicht existiert
        return f"'{attr}' ist nicht vorhanden!"

    def __getattribute__(self, attr):
        print(f"Zugriff auf: {attr}")
        # Es ruft die Standard-Implementierung aus der Elternklasse (object) auf
        # – ohne sich selbst erneut zu triggern.
        return super().__getattribute__(attr)

    def __setattr__(self, attr, value):
        # Wird aufgerufen, wenn ein Attribut gesetzt wird
        print(f"Setze Attribut: {attr} = {value}")
        # Vermeide Rekursion &  Endlosschleife: direktes Setzen durch die Elternklasse (object)
        # Ruft die originale __setattr__-Methode aus der object-Klasse auf
        super().__setattr__(attr, value)

    def __delattr__(self, attr):
        # Wird aufgerufen, wenn ein Attribut gelöscht wird
        print(f"Lösche Attribut: {attr}")
        super().__delattr__(attr)

    def __call__(self, text):
        # Die Methode __call__ macht ein Objekt aufrufbar wie eine Funktion.
        # Statt obj.mach_was("Text") kann man einfach obj("Text") schreiben.
        return f"Aufruf mit: {text}"

# Anwendung
obj = Beispiel()

print(obj.name)           # Zugriff auf vorhandenes Attribut → Ausgabe: Python

print(obj.sprache)        # Zugriff auf nicht vorhandenes Attribut → __getattr__ → 'sprache' ist nicht vorhanden!

obj.version = "3.12"      # __setattr__ wird aufgerufen → Ausgabe: Setze Attribut: version = 3.12

del obj.name              # __delattr__ wird aufgerufen → Ausgabe: Lösche Attribut: name

print(obj("Läuft!"))      # __call__ wird aufgerufen → Ausgabe: Aufruf mit: Läuft!




"""
Die Methode __call__ macht ein Objekt aufrufbar wie eine Funktion.
Statt obj.mach_was("Text") kann man einfach obj("Text") schreiben.
Das ist praktisch, wenn ein Objekt ein zentrales Verhalten ausführen soll.
Im Hintergrund wird bei obj("Text") automatisch obj.__call__("Text") aufgerufen.

__call__ wird selten im Alltagscode gebraucht –
aber es ist sehr nützlich in bestimmten Situationen, vor allem bei:

Funktionalen Objekten, z.B. Parser, Konverter, Formatierer

Zustandsbehafteten Objekten, die sich wie Funktionen verhalten

Machine-Learning-Modellen, z.B. model(input)

APIs oder DSLs, wo elegante, kurze Aufrufe gewünscht sind
"""