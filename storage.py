
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data.json"


def load_employee():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            employees = json.load(file)

            if not isinstance(employees, list):
                print("Error: JSON data must be a list of employees.")
                return None

            if not all(isinstance(emp, dict) for emp in employees):
                print("Error: Invalid employee data in JSON file.")
                return None

            return employees

    except FileNotFoundError:
        # No saved data yet
        return []

    except json.JSONDecodeError as e:
        print("Error: data.json contains invalid JSON.")
        print("Details:", e)
        return None

    except OSError as e:
        print("Error reading data.json:", e)
        return None


def save_employee(employee):
    employees = load_employee()

    if employees is None:
        print("Cannot save employee because the data file has an error.")
        return False

    for emp in employees:
        if emp.get("empId") == employee.empId:
            print("Employee ID already exists.")
            return False

    employees.append(employee.storeAsDict())

    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(employees, file, indent=4)

        print("Employee added successfully.")
        return True

    except (OSError, TypeError, ValueError) as e:
        print("Error saving employee:", e)
        return False


def update_employee(emp_id, name, age, salary):
    employees = load_employee()

    if employees is None:
        print("Cannot update employee because the data file has an error.")
        return False

    for emp in employees:
        if emp.get("empId") == emp_id:
            emp["empName"] = name
            emp["empAge"] = age
            emp["empSalary"] = salary

            try:
                with open(DATA_FILE, "w", encoding="utf-8") as file:
                    json.dump(employees, file, indent=4)

                print("Employee updated successfully.")
                return True

            except (OSError, TypeError, ValueError) as e:
                print("Error updating employee:", e)
                return False

    print("Employee not found.")
    return False


def delete_employee(emp_id):
    employees = load_employee()

    if employees is None:
        print("Cannot delete employee because the data file has an error.")
        return False

    for emp in employees:
        if emp.get("empId") == emp_id:
            employees.remove(emp)

            try:
                with open(DATA_FILE, "w", encoding="utf-8") as file:
                    json.dump(employees, file, indent=4)

                print("Employee deleted successfully.")
                return True

            except (OSError, TypeError, ValueError) as e:
                print("Error deleting employee:", e)
                return False

    print("Employee not found.")
    return False
