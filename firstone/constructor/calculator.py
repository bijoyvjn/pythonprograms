class Calculator:
    def __init__(self,one,two):
        self.one=one
        self.two=two
    def printval(self):
        print(self.one+self.two)
        print(self.one-self.two)
        print(self.one*self.two)
        print(self.one/self.two)

c=Calculator(5,4)
c.printval()