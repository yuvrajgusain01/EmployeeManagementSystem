from miniProject.emp import Employee
from miniProject.storage import (
    save_employee,
    load_employee,
    update_employee,
    delete_employee
)


def main():
    while True:
        print("\n---------- EMPLOYEE MANAGEMENT SYSTEM ----------")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. Show Employee Details")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            empId = input("Enter Employee ID: ").strip()
            name = input("Enter Employee Name: ").strip()

            if not empId or not name:
                print("Employee ID and name cannot be empty.")
                continue

            try:
                age = int(input("Enter Employee Age: "))
                salary = int(input("Enter Employee Salary: "))

                if age <= 0 or salary < 0:
                    print("Age must be positive and salary cannot be negative.")
                    continue

            except ValueError:
                print("Age and salary must be valid integers.")
                continue

            employee = Employee(empId, salary, name, age)

            if save_employee(employee):
                print("Employee details saved successfully.")

        elif choice == 2:
            empId = input("Enter Employee ID to delete: ").strip()

            if not empId:
                print("Employee ID cannot be empty.")
                continue

            if delete_employee(empId):
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")

        elif choice == 3:
            empId = input("Enter Employee ID to update: ").strip()

            if not empId:
                print("Employee ID cannot be empty.")
                continue

            employees = load_employee()

            if not any(emp["empId"] == empId for emp in employees):
                print("Employee not found.")
                continue

            name = input("Enter new Employee Name: ").strip()

            if not name:
                print("Employee name cannot be empty.")
                continue

            try:
                age = int(input("Enter new Employee Age: "))
                salary = int(input("Enter new Employee Salary: "))

                if age <= 0 or salary < 0:
                    print("Age must be positive and salary cannot be negative.")
                    continue

            except ValueError:
                print("Age and salary must be valid integers.")
                continue

            if update_employee(empId, name, age, salary):
                print("Employee updated successfully.")

        elif choice == 4:
            employees = load_employee()

            if not employees:
                print("No employees saved.")
            else:
                for emp_data in employees:
                    employee = Employee(
                        emp_data["empId"],
                        emp_data["empSalary"],
                        emp_data["empName"],
                        emp_data["empAge"]
                    )

                    print("\n------------------------------")
                    employee.display()

        elif choice == 5:
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()