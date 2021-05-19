class Student:
    college="elephant rock"
    def details(self,id,name):
        self.i=id
        self.n=name
    def display(self):
        print("id:",self.i)
        print("name:",self.n)
        print("college:",Student.college)
s=Student()
s.details(4,"bijoy")
s.display()

#instance variable related to methods
#class variables realared to class