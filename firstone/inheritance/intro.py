#Single inheritance

class Person:               #super class/base class/parent class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)

class Student(Person):      #derived class/sub class/child class
    def print(self,department,college):
        self.department=department
        self.college=college
        print(self.department)
        print(self.college)


p=Person()
p.details("bijoy",5,"male")
st=Student()
st.print("lkg","anganvaady")
st.details("bijoy",1,"male")