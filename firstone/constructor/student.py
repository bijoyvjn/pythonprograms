class Student:
    school="elephant rock"
    def __init__(self,id,name,standard):
        self.id=id
        self.name=name
        self.standard=standard
    def printval(self):
        print(self.id)
        print(self.name)
        print(self.standard)
        print(Student.school)
s=Student(1,"bijoy",10)
s.printval()
