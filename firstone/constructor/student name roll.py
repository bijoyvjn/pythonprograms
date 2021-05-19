class Student():
    def details(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll

        print(self.name)
        print(self.age)
        print(self.roll)
    def __str__(self):
        return self.name+str(self.roll)

s=Student()
s.details("boy",12,3)
print(s)