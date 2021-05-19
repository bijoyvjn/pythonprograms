class Driving:
    def start(self):
        print("car starting")
    def accelarate(self):
        print("car moving")

class Riding:
    def start(self):
        print("bike starting")
    def accelarate(self):
        print("bike moving")

class Person:
    def drive(self,vehi):
        vehi.start()
        vehi.accelarate()

p=Person()
d=Driving()
p.drive(d)