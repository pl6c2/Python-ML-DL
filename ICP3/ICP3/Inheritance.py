class Employee:
    count=0
    sum=0
    def __init__(self, name, family, salary, department):
        self.__class__.count= self.__class__.count+1
        self.name=name
        self.family=family
        self.salary=salary
        self.department=department

    def avgsalary(self):
        for i in employeeList:
            self.__class__.sum= self.__class__.sum + i.salary
        print('Average is',self.__class__.sum/self.__class__.count)

class FullTimeEmployee(Employee):
    pass

f = FullTimeEmployee("prem", "lingamgunta", 100, "cs")
f1 = FullTimeEmployee("premchand", "l", 300, "cs")
f2 = FullTimeEmployee("chand", "lin", 200, "CSE")


employeeList = []
employeeList.append(f)
employeeList.append(f1)
employeeList.append(f2)


f.avgsalary()
