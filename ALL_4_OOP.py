# Project On All 4 OOP Combine

from abc import ABC, abstractmethod             # Import Abstraction

# ==========================================
# ABSTRACTION
# ==========================================

class Employee(ABC):

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age

        # ==========================================
        # ENCAPSULATION
        # ==========================================
        self.__salary = salary

    # Get the private salary
    def get_salary(self):
        return self.__salary

    # Change the private salary
    def set_salary(self, salary):

        if salary >= 0:
            self.__salary = salary
            print("Salary updated successfully.")

        else:
            print("Salary cannot be negative.")

    # Every employee must have a work() method
    @abstractmethod
    def work(self):
        pass


# ==========================================
# INHERITANCE + POLYMORPHISM
# ==========================================

class Developer(Employee):

    def work(self):
        print(f"{self.name} is writing Python code.")


class Designer(Employee):

    def work(self):
        print(f"{self.name} is creating UI designs.")


class Manager(Employee):

    def work(self):
        print(f"{self.name} is managing the team.")


# ==========================================
# EMPLOYEE LIST
# ==========================================

employees = []


# ==========================================
# ADD EMPLOYEE
# ==========================================

def add_employee():

    print("\n===== Add Employee =====")
    print()
    name = input("Enter employee name: ")

    age = int(input("Enter employee age: "))

    salary = float(input("Enter employee salary: "))

    print("\nChoose employee type:")
    print()
    print("1. Developer")
    print("2. Designer")
    print("3. Manager")
    print()
    choice = input("Enter choice: ")

    if choice == "1":

        employee = Developer(name, age, salary)

    elif choice == "2":

        employee = Designer(name, age, salary)

    elif choice == "3":

        employee = Manager(name, age, salary)

    else:

        print("Invalid employee type.")
        return

    employees.append(employee)

    print("\nEmployee added successfully!")


# ==========================================
# VIEW EMPLOYEES
# ==========================================

def view_employees():

    print("\n===== Employee List =====")
    print()
    if not employees:

        print("No employees found.")
        return

    for employee in employees:

        print("--------------------------")

        print(f"Name: {employee.name}")
        print(f"Age: {employee.age}")
        print(f"Salary: ${employee.get_salary()}")

        # POLYMORPHISM
        employee.work()

    print("--------------------------")


# ==========================================
# SEARCH EMPLOYEE
# ==========================================

def search_employee():

    print("\n===== Search Employee =====")
    print()
    name = input("Enter employee name: ")

    for employee in employees:

        if employee.name.lower() == name.lower():

            print("\nEmployee Found!")
            print("--------------------------")
            print(f"Name: {employee.name}")
            print(f"Age: {employee.age}")
            print(f"Salary: ${employee.get_salary()}")

            employee.work()

            return

    print("Employee not found.")


# ==========================================
# UPDATE SALARY
# ==========================================

def update_salary():

    print("\n===== Update Salary =====")
    print()
    name = input("Enter employee name: ")

    for employee in employees:

        if employee.name.lower() == name.lower():

            print(f"Current salary: ${employee.get_salary()}")

            new_salary = float(
                input("Enter new salary: ")
            )

            employee.set_salary(new_salary)

            return

    print("Employee not found.")


# ==========================================
# REMOVE EMPLOYEE
# ==========================================

def remove_employee():

    print("\n===== Remove Employee =====")
    print()
    name = input("Enter employee name: ")

    for employee in employees:

        if employee.name.lower() == name.lower():

            employees.remove(employee)

            print(f"{employee.name} has been removed successfully.")

            return

    print("Employee not found.")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n================================")
    print("    EMPLOYEE MANAGEMENT SYSTEM")
    print("================================")
    print()
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Remove Employee")
    print("6. Exit")
    print()
    choice = input("Enter your choice: ")

    if choice == "1":

        add_employee()

    elif choice == "2":

        view_employees()

    elif choice == "3":

        search_employee()

    elif choice == "4":

        update_salary()

    elif choice == "5":

        remove_employee()

    elif choice == "6":
        print()
        print("Thank you for using the Employee Management System. Have a great day!")
        break

    else:

        print("Invalid choice. Please try again.")