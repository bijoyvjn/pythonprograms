#18

lst=['php','w3r','Python','abcd','Java','aaa']
print("origingal list",lst,end=' ')
print()

print("reversed list",end=' : ')
lst1=[]
for i in lst:
    lst1.append(i[::-1])
print(lst1,end=' ')
print()

for i in lst:
    for j in lst1:
        if i in j:
            print(i,end=' ')



