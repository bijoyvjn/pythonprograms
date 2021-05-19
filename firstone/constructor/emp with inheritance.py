class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printd(self):
        print(self.name)
        print(self.age)
class Employee(Person):
    def __init__(self,salary,pos,name,age):
        super().__init__(name,age)
        self.salary=salary
        self.pos=pos
    def print(self):
        print(self.salary)
        print(self.pos)
e=Employee(25000,20,"bijoy",23)
e.printd()
e.print()