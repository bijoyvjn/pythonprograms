class Parent():
    def m1(self,name):
        self.name=name
        print(self.name)

class Child(Parent):
    def m2(self,age):
        self.age=age
        print(self.age)

class Subchild(Child):
    def m3(self,relation):
        self.relation=relation
        print(self.relation)

p=Parent()
p.m1("bijoy")
print("...................")
c=Child()
c.m1("bijoy")
c.m2(22)
print("....................")
s=Subchild()
s.m1("bijoy")
s.m2(22)
s.m3("dad")