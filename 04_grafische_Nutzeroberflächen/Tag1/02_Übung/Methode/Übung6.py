class Employee:
    employee_count = 0

    def __init__(self, name, stelle) -> None:
        self.name = name
        self.stelle = stelle
        Employee.employee_count += 1

    def display_employee_info(self):
        print(f'{self.name} arbeitet als {self.stelle}.')

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count


Alice = Employee('Alice', 'Manager')
Alice.display_employee_info()

Bob = Employee('Bob', 'Kocher')
Bob.display_employee_info()
print(Employee.get_employee_count())
