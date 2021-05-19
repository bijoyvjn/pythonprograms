sub1=int(input("Enter the mark"))
sub2=int(input("Enter the mark"))
sub3=int(input("Enter the mark"))
sub4=int(input("Enter the mark"))
total=sub1+sub2+sub3+sub4
print(total)
if (total>=180) & (total<=200):
    print("A+")
elif(total>=160) & (total<=179):
    print("A")
elif(total>=140) & (total<=159):
    print("B+")
elif(total>=120) & (total<=149):
    print("B")
elif(total>=100) & (total<=119):
    print("C+")
elif(total>=80) & (total<=99):
    print("C")
elif(total<=149):
    print("fail")
else:
    print("invalid input")