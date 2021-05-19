lst=[1,2]
lst1=[10,20]

out=[(first,second) for first in lst for second in lst1]
print(out)

# for first in lst:
#     for second in lst1:
#         print((first,second))