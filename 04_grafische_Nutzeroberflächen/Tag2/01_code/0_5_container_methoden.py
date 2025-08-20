class Einkaufsliste:
    def __init__(self):
        # Konstruktor: Erstellt eine Liste mit 3 Anfangswerten
        self.items = ["Brot", "Milch", "Käse"]

    def __getitem__(self, index):
        # Wird aufgerufen, wenn man z.B. liste[0] schreibt
        print("bin daaa 1")
        return self.items[index]

    def __setitem__(self, index, value):
        # Wird aufgerufen, wenn man z.B. liste[1] = "Saft" schreibt
        print("bin daaa")
        self.items[index] = value

    def __delitem__(self, index):
        # Wird aufgerufen, wenn man z.B. del liste[2] schreibt
        print("muss weg")
        del self.items[index]

    def __len__(self):
        # Ermöglicht die Verwendung von len(liste)
        return len(self.items)

    def __reversed__(self):
        # Wird verwendet, wenn man reversed(liste) aufruft
        return reversed(self.items)

    def __str__(self):
        # Gibt die Einkaufsliste als String zurück, z.B. "['Brot', 'Milch', 'Käse']"
        return f"{self.items}"

# Beispielverwendung:
liste = Einkaufsliste()

#print(liste[0])
liste[1] = "Saft"
print(liste[1])
del liste[2]
print(len(liste))
print(list(reversed(liste)))
print(liste)

