class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary , age):
        self.name = name
        self.salary = salary
        self.age = age
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary , ", Age:" ,self.age)

def main():
    #This would create first object of Employee class"
    emp1 = Employee("Zara", 2000 , 28)
    #This would create second object of Employee class"
    emp2 = Employee("Manni", 5000 , 31)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print ("Total Employee %d" % Employee.empCount)
    print(hasattr(emp1, 'height'))
    print(getattr(emp1, 'salary'))
    setattr(emp1, 'age', 23)
    print (emp1.age)

main()