class Employee:
    company="c p"
    def details(self,id,name,salary,job):
        self.id=id
        self.name=name
        self.salary=salary
        self.job=job
    def display(self):
        print("id",self.id)
        print("name",self.name)
        print("salary",self.salary)
        print("company",Employee.company)
        print("job",self.job)
e=Employee()
e1=Employee()
e.details(3,"bijoy",60000,"HR")
e.display()
e1.details(5,"athira",5000,"Adichu vaarunna aal")
e1.display()
