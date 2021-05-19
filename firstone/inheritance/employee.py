class Person:
    def details(self,name,age,gender):
        self.n=name
        self.a=age
        self.g=gender
        print(self.n)
        print(self.a)
        print(self.g)
class Employee(Person):
    def print(self,pos,salary):
        self.w=pos
        self.s=salary
        print(self.w)
        print(self.s)

p=Person()
p.details("bijoy",4,"male")
e=Employee()
e.details("bijoy",5,"male")
e.print("anganvaady",3)