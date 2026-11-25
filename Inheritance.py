class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_role(self):
        print(f"Employee: {self.name} | Role: General Staff | Salary: ₹{self.salary}")

    def __add__(self, other):
        return self.salary + other.salary

    def __gt__(self, other):
        return self.salary > other.salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_role(self):
        print(f"Manager: {self.name} | Department: {self.department} | Salary: ₹{self.salary}")


emp1 = Employee("Arun", 45000)
mgr1 = Manager("Divya", 75000, "IT")

print("--- Inheritance & Method Overriding ---")
emp1.display_role()
mgr1.display_role()

print("\n--- Operator Overloading ---")
print(f"Combined Salary (emp1 + mgr1): ₹{emp1 + mgr1}")
print(f"Does Manager earn more than Employee? (mgr1 > emp1): {mgr1 > emp1}")