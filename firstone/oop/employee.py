class Employee:
    def details(self,id,name,salary,age,department,company):
        self.id=id
        self.name=name
        self.salary=salary
        self.age=age
        self.department=department
        self.company=company
    def print(self):
        print(self.id)
        print(self.name)
        print(self.salary)
        print(self.age)
        print(self.department)
        print(self.company)
e=Employee()
e.details(1,"bijoy",80000,25,"it","world no1")
e.print()

        # name id salary age department company