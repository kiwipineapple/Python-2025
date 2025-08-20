import enum


class State(enum.IntEnum):
    OFF = 0
    ON = 1


class Role(enum.IntEnum):
    CEO = 1
    DEV = 2
    PRESIDENT = 3


class Employee:
    def __init__(self, name, role: Role):
        self.name = name
        self.role = role


bob = Employee("Bob", Role.DEV)
print(bob.role)

State.ON  # 1
