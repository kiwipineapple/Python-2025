class Widget:
    def draw(self):
        raise NotImplementedError("Subclasses should implement this!")

class Button(Widget):
    def draw(self):
        return "Drawing a Button"

class TextField(Widget):
    def draw(self):
        return "Drawing a TextField"

widgets = [Button(), TextField()]

for widget in widgets:
    print(widget.draw())

"""
Erklärung: Hier erben die Klassen Button und TextField von der Basisklasse Widget und 
überschreiben die Methode draw. 

Der Polymorphismus ermöglicht es, dass die Methode draw für jedes 
Widget-Objekt entsprechend seiner spezifischen Implementierung aufgerufen wird.

"""
