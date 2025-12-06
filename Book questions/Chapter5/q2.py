class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    @classmethod
    def from_string(cls, employee_str):
        name, emp_id, salary = employee_str.split(',')
        return cls(name, emp_id, int(salary))
    
    def display_employee_info(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Salary: ${self.salary}")

emp1 = Employee("John Doe", "E123", 50000)
emp1.display_employee_info()

emp2 = Employee.from_string("John Doe,E123,50000")
emp2.display_employee_info()