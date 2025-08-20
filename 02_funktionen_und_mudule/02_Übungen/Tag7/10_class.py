# Ü1
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def vorstellen(self):
#         print(f'{self.name} is {self.age} years old.' )

# infos = Person('Anna', 28)
# infos.vorstellen()

# Ü2
class student:
    def __init__(self, name, matrikelnummer):
        self.name = name
        self.matrikelnummer = matrikelnummer
        self.noten = []

    def add_note(self, note):
        self.noten.append(note)

    def durchschnittnote(self):
        if len(self.noten) > 0:
            return sum(self.noten) / len(self.noten)