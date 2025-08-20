class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def birthday(self) -> None:
        self.age += 1
        print(f'{self.name} is {self.age} years old.')


person1 = Person('Alice', 10)
print(person1.birthday())
