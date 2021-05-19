class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
    def val(self):
        print(self.name)
        print(self.age)
a=Person()
a.details("bijoy",23)
a.val()