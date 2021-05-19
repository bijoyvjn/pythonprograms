#person parent child student
#parent _ person    child_person    student_child

class Person():
    def details(self,name):
        self.name=name
        print(self.name)

class Parent(Person):
    def rel(self,relation):
        self.relation=relation
        print(self.relation)

class Child(Person):
    def chil(self,cname):
        self.cname=cname
        print(self.cname)

class Student(Child):
    def info(self,school):
        self.school=school
        print(self.school)

p=Person()
p.details("bijoy")
print(".................")
p1=Parent()
p1.details("bijoy")
p1.rel("dad")
print("...................")
c=Child()
c.details("bijoy")
c.chil("angel")
print("....................")
s=Student()
s.details("bijoy")
s.chil("angel")
s.info("little flower")