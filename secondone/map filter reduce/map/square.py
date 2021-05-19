lst=[1,2,3,4,5]

# sq=lambda num:num**2
# print(sq(5))

sq=list(map(lambda num:num**2,lst))
print(sq)