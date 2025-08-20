"""
Bidirektionale Assoziation

Beide Klassen wissen voneinander und können
miteinander interagieren.

Employee kennt Company
Company kennt Employee(s)
"""

from __future__ import annotations


class Company:
    def __init__(self, name: str):
        self.name = name
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        employee.company = self

    def __str__(self) -> str:
        return self.name


class Employee:
    def __init__(self, name: str):
        self.name = name
        self.company: Company | None = None

    def __str__(self) -> str:
        return self.name


bob = Employee("Bob")
alice = Employee("Alice")
bmw = Company(name="BMW")
bmw.add_employee(bob)
bmw.add_employee(alice)

print(f"{bob} arbeitet bei {bob.company.name}")

print("Angestellte von BMW:")
for employee in bmw.employees:
    print(employee.name)
