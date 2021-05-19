class Person():
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Employee():
    def work(self,pos):
        self.pos=pos
        print(self.pos)
class Salary(Person,Employee):
    def info(self,money):
        self.money=money
        print(self.money)

p=Person()
p.details("me",22)
print("...................")
e=Employee()
e.work("HR")
print("....................")
s=Salary()
s.details("mine",23)
s.work("Chair")
s.info(201)