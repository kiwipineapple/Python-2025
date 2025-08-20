class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    def bellen(self):
        print(f"{self.name} bellt!")
        print(f"{self.alter}")

mein_hund = Hund("Bello", 3)
mein_hund.bellen()  # Ausgabe: Bello bellt!

hund_2 = Hund("Waldi",5)
print(hund_2.alter)