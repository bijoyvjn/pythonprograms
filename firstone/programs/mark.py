class Student:
    def info(self,name,roll,std,mark):
        self.name=name
        self.roll=roll
        self.std=std
        self.mark=mark

    def print(self):
        print("name:",self.name)
        print("roll:",self.roll)
        print("std:",self.std)
        print("mark:",self.mark)

    def __str__(self):
        return self.name

f=open("mark","r")
for i in f:
    data=i.split(",")

    name=data[0]
    roll=data[1]
    std=data[2]
    mark=data[3]

    s=Student()
    s.info(name,roll,std,mark)
    print(s)
    s.print()