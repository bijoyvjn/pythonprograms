salary=int(input("Enter hte salary"))
exp=int(input("Enter the experience"))

print("your salary is",salary)
print("your experience is",exp)

if(exp>=5):
    bon = (5 / 100) * salary
    print("your bonus bonus is", bon)
    final=salary+bon
    print("The salary with bonus is",final)
else:
    print("There is no bonus and salary is ",salary)
