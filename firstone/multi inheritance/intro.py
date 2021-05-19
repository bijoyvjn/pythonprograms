class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Mobile:
    def print(self):
        print("i have one plus")
class Child(Person,Mobile):
    def info(self,college,place):
        self.college=college
        self.place=place
        print(self.college)
        print(self.place)
p=Person()
p.details("bijoy",22)
m=Mobile()
m.print()
c=Child()
c.details("thor",3500)
c.print()
c.info("world","hammer")