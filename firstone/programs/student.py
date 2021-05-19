class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printval(self):
        print("name:",self.name)
        print("age:",self.age)

    def __str__(self):
        return self.name

f=open("student","r")
for line in f:
    data=line.split(",")
    name=data[0]
    age=data[1]
    s=Person(name,age)
    print(s)
    s.printval()