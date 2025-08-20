class Datei:
    def lesen(self):
        raise NotImplementedError("Subclasses should implement this!")


class TextDatei(Datei):
    def lesen(self):
        return "Lesen von Textdatei"


class BinärDatei(Datei):
    def lesen(self):
        return "Lesen von Binärdatei"


dateien = [TextDatei(), BinärDatei()]

for datei in dateien:
    print(datei.lesen())
