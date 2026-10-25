import json


def load_employee():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_employee(employee):
    employees = load_employee()

    for emp in employees:
        if emp["empId"] == employee.empId:
            print("Employee ID already exists.")
            return False

    employees.append(employee.storeAsDict())

    with open("data.json", "w") as file:
        json.dump(employees, file, indent=4)

    return True


def update_employee(emp_id, name, age, salary):
    employees = load_employee()

    for emp in employees:
        if emp["empId"] == emp_id:
            emp["empName"] = name
            emp["empAge"] = age
            emp["empSalary"] = salary

            with open("data.json", "w") as file:
                json.dump(employees, file, indent=4)

            return True

    return False


def delete_employee(emp_id):
    employees = load_employee()

    for emp in employees:
        if emp["empId"] == emp_id:
            employees.remove(emp)

            with open("data.json", "w") as file:
                json.dump(employees, file, indent=4)

            return True

    return False