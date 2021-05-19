class Person():
    def show(self,n1):
        self.n1=n1
        print(self.n1)
class Student(Person):
    def  show(self,n2,n3):
        self.n2=n2
        self.n3=n3
        print(self.n2+self.n3)
p=Student()
p.show(4,5)