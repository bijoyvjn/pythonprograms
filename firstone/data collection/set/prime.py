s={4,5,6,3,2,8,9,7}
prime=set()
non=set()
for i in s:
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                non.add(i)
                break
            else:
                prime.add(i)
print(prime)
print(non)
