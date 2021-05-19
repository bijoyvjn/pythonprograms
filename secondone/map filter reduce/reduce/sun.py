# we should import reduce functionality, the functionality module is inside the 'functools'
# we should pass 2 arguments
# only we can pass numbers not strings

from functools import reduce
lst=[1,2,3,4,5,6]

total=reduce(lambda num1,num2:num1+num2,lst)
print("total is:",total)

highest=reduce(lambda num3,num4:num3 if num3>num4 else num4,lst)
print("highest number is:",highest)
