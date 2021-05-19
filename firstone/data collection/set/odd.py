s={5,2,1,4,6,9,7,3}
odd=set()
even=set()

for i in s:
    if (i%2==0):
        even.add(i)
    else:
        odd.add(i)
print("odd elements",odd)
print("even elements",even)