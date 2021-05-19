class Add():
    def two(self,one,two):
        self.one=one
        self.two=two
    def three(self):
        print(self.one+self.two)

c=Add()
c.two(2,5)
c.three()