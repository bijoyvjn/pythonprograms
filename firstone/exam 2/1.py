class Vehicle:
    def det(self,number,color):
        self.number=number
        self.color=color
        print(self.number)
        print(self.color)
class Bus(Vehicle):
    def info(self,owner,condition):
        self.owner=owner
        self.condition=condition
        print(self.owner)
        print(self.condition)
b=Bus()
b.det("kl88585","black")
b.info("bijoy","good")