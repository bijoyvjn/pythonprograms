class Pych:
    def comp(self):
        print("pycharm compilation")
    def exe(self):
        print("pycharm execution")

class Idle:
    def comp(self):
        print("idle compilation")
    def exe(self):
        print("idle execution")

class Programmer:
    def coding(self,ide):
        ide.comp()
        ide.exe()

p=Programmer()
pl=Idle()
p.coding(pl)