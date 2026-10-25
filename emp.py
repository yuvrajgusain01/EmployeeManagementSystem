class Employee:
    def __init__(self, empId, empSalary, empName, empAge):
        self.empId = empId
        self.empSalary = empSalary
        self.empName = empName
        self.empAge = empAge

    def storeAsDict(self):
        return {
            "empId": self.empId,
            "empSalary": self.empSalary,
            "empName": self.empName,
            "empAge": self.empAge
        }

    def display(self):
        print(f"Employee ID: {self.empId}")
        print(f"Employee Name: {self.empName}")
        print(f"Employee Age: {self.empAge}")
        print(f"Employee Salary: {self.empSalary}")