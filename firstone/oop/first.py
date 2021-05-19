# class : design pattern
# object : real world entity
# references : name that refers a memory location of a object
#class name must start in capital letters

class Person:
    def walk(self):
        print("person is walking")
    def jump(self):
        print("person is jumping")
a=Person()                #a is the object reference of class person
a.walk()
a.jump()