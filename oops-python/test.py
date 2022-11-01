class Employee:
    def role(self):
        self.name="Azhar"
        print(self.name)
        self.age=23
        print(self.age)
    def details(self):
        print(self.name)
        print(self.age)
employee=Employee()
employee.role()
employee.details()
Employee.role(employee)