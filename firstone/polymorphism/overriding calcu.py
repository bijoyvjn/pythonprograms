class Num:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def add(self):
        print(self.n1+self.n2)

class Sub(Num):

    def add(self):
        print(self.n1-self.n2)

s=Sub(5,3)
s.add()