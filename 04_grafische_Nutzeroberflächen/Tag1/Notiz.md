# abstrakt method immer import ABC, abstractmethod
-- @abstractmethod func defined a function nur mit pass.

```python
class Person:
    language = "Global."

    def __init__(self, lang):
        self.language = lang + "."


class Student(Person):
    language = "Deutsch."

    @classmethod
    def sprache(cls, self):
        print(cls.language)

    @staticmethod
    def echo(Student):
        print(Student.language)


p = Person("English")
s = Student("Französisch")

s.sprache(p)
s.echo(p)
print(p.language)
print(Person.language)
```
**output**
```python
Deutsch
English.
Englisch.
Global.
```