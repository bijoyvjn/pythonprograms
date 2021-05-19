class Parent:
    def prorperties(self):
        print("buy one get one offer")


    def marry(self):
        print("married an angel")

class Child(Parent):

    def marry(self):
        print("married a marvelous angel")

c=Child()
c.marry()