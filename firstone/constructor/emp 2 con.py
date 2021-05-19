class Employee():
    def __init__(self,name,age,salary,pos):
        self.name=name
        self.age=age
        self.salary=salary
        self.pos=pos
    def printd(self):
        print("Employee name:",self.name)
        print("Employee age:",self.age)
        print("Employee salary:",self.salary)
        print("Employee position:",self.pos)
    def __str__(self):
        # return self.name              name
        # return str(self.age)          age __ int value have to convert in string
        return self.name+":"+str(self.age)+":"+str(self.salary)

e=Employee("bijoy",20,25000,"HR")
e.printd()
print(e)