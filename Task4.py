import random

cities = ["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgon", "Hyderabad"]

class Employee:
    def __init__(self, emp_id, emp_location, emp_salary):
        self.emp_id = emp_id
        self.emp_location = emp_location
        self.emp_salary = emp_salary

    def __str__(self):
        return f"Emp ID: {self.emp_id}, Location: {self.emp_location}, Salary: {self.emp_salary}"

def generate_employee_details(num_employees):
    for _ in range(num_employees):
        emp_id = random.randint(1, 9999)
        emp_location = random.choice(cities)
        emp_salary = random.randint(20000, 150000)
        
        employee = Employee(emp_id, emp_location, emp_salary)

        yield employee

num_employees = int(input("Enter the number of employee details to generate: "))
employee_generator = generate_employee_details(num_employees)

print("\nGenerated Employee Details:")
for i in range(num_employees):
    employee = next(employee_generator)
    print(employee)
