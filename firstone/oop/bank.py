class Bank:
    bankname="elephant rock"
    def creation(self):
        name=input("enter the name")
        age=int(input("enter the age"))
        print(name,age,Bank.bankname)
    def deposite(self,money):
        self.money = money
        money=int(input("enter the amount you want to enter"))
        print("you deposited",money)
        print("now balance",money)
    def withdraw(self,withdraw):
        self.withdraw=withdraw
        self.withdraw=int(input("how much you want to withdraw"))
        print("you withdrawn",self.withdraw,"rupees")
        print("now balance is ",self.money-self.withdraw)


b=Bank()
opt=int(input("1. for creation 2. for deposite 3. for withdraw"))
if opt==1:
    b.creation()
elif opt==2:
    b.deposite(999)
elif opt==3:
    b.withdraw(999)
else:
    print("invalid input")