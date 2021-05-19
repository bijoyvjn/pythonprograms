age=int(input("Enter your age"))
sex=input("Enter your sex")
mar=input("Enter your marital status")

print(age,sex,mar)

if(sex=='F'):
    print("Work only in urban areas")
elif(sex=='M') &(age>=20)&(age<=40):
    print("work in anywhere")
elif(sex=='M')&(age>=40)&(age<=60):
    print("work in urban areas")
else:
    print("ERROR")