
import json


def load_employee():
    try:
        with open("data.json", "r") as file:
            employees = json.load(file)

            if not isinstance(employees, list):
                print("Error: JSON data must contain a list of employees.")
                return None

            return employees

    except FileNotFoundError:
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
        print("Cannot save employee because the data file could not be read.")
        return False

    for emp in employees:
        if emp["empId"] == employee.empId:
            print("Employee ID already exists.")
            return False

    employees.append(employee.storeAsDict())

    try:
        with open("data.json", "w") as file:
            json.dump(employees, file, indent=4)

        return True

    except (OSError, TypeError, ValueError) as e:
        print("Error saving employee data:", e)
        return False


def update_employee(emp_id, name, age, salary):
    employees = load_employee()

    if employees is None:
        print("Cannot update employee because the data file could not be read.")
        return False

    for emp in employees:
        if emp.get("empId") == emp_id:
            emp["empName"] = name
            emp["empAge"] = age
            emp["empSalary"] = salary

            try:
                with open("data.json", "w") as file:
                    json.dump(employees, file, indent=4)

                return True

            except (OSError, TypeError, ValueError) as e:
                print("Error updating employee data:", e)
                return False

    return False


def delete_employee(emp_id):
    employees = load_employee()

    if employees is None:
        print("Cannot delete employee because the data file could not be read.")
        return False

    for emp in employees:
        if emp.get("empId") == emp_id:
            employees.remove(emp)

            try:
                with open("data.json", "w") as file:
                    json.dump(employees, file, indent=4)

                return True

            except (OSError, TypeError, ValueError) as e:
                print("Error deleting employee data:", e)
                return False

    return False
