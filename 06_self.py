class Employee:
    company = "Google"
    def getsSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100000
harry.getsSalary() # Employee.getSalary(harry)