num1=int(input("enter the starting range"))
num2=int(input("enter the last range"))
for i in range(num1,num2+1):
    if(i%2==1):
        for j in range(num1,num2+1):
            print()
            for k in range(0,j):
                print(i,end=" ")
    else:
        for j in range(num1,num2+1):
            print()
            for k in range(num2+1,j,-1):
                print(i,end=" ")