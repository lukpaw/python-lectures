"""
==========================
Task instructions:
==========================
This program defines two classes using inheritance:
  - Employee: A base class representing a generic employee with basic information.
      - Fields: name (str), department (str)
      - Method: get_info() - Returns a string containing the employee's information (name and department).
  - Manager: A derived class inheriting from Employee, with additional management responsibilities.
      - Additional fields: team_size (int)
      - Method: get_info() (overrides base class method) - Returns a string containing all manager information (including inherited employee info).

==========================
Usage:
==========================
employees = []

employees.append(Employee("John", "Sales"))
employees.append(Employee("Kate", "Marketing"))
employees.append(Manager("David", "Sales", 7))
employees.append(Manager("George", "Marketing", 6))

# Print information for all employees (including managers)
for employee in employees:
    print(f"{employee.get_info()}\n")


==========================
Example Output:
==========================
Name: John
Department: Sales

Name: Kate
Department: Marketing

Name: David
Department: Sales
Team Size: 7

Name: George
Department: Marketing
Team Size: 6
"""