total=int(input("Enter the number of classes"))
attend=int(input("student attended classes"))
avg=(attend/total)*100
print(avg)
if(avg>=75):
    print("stdent can attend the exam")
else:
    print("stdent cannot attend the exam")