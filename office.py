class Office:
    numberOfEmployees=0
    def __init__(self,officeName,officeEmployee):
        self.officeName=officeName
        self.officeEmployee=officeEmployee

    def getAllEmployees(self):
        employees = []
        for i in self.officeEmployee:
            employees.append(i.name)
        return employees

    def getEmployee(self, employeeId):
        for i in self.officeEmployee:
            if i.id == employeeId:
                return i.name

    def getEmployeeObject(self, employee_id):
        for i in self.officeEmployee:
            if i.id == employee_id:
                return i

    def hire(self, Employee):
        self.officeEmployee.append(Employee)
        Office.numberOfEmployees += 1

