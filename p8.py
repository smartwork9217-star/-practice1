"""Employee(name, salary) with yearly_pay() = salary x 12
Manager(Employee) adds a bonus
Manager overrides yearly_pay(): parent's pay + bonus (use super())
Loop over both and print name and yearly pay
Print isinstance(manager, Employee)"""

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_pay(self):
        return self.salary * 12

class Manager(Employee):

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def yearly_pay(self):
        return super().yearly_pay() + self.bonus

staff = [Employee("Sara", 80000), Manager("Omar", 150000, 200000)]
for emp in staff:
    print(emp.name, emp.yearly_pay())
print(isinstance(staff[1], Employee))