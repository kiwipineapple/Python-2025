"""
Aggregate sind eine Assoziation und definiert durch
eine Teil-Ganzes-Beziehung. Das Teil existiert weiter, wenn das
Ganze gelöscht wird.

Eine Schule hat Schüler (und ein Schüler kann ohne die Schule existieren).

"""


class Student:
    """Student ist der Teil...."""

    def __init__(self, name):
        self.name = name
        self.school = None


class School:
    """Schule ist das Ganze..."""

    def __init__(self, name):
        self.name = name
        self.students = []


bob = Student("Bob")  # Bob lebt weiter, nach Zerstörung der Schule
school = School("WBS")
school.students.append(bob)
del school

print(bob)  # Hurra!
