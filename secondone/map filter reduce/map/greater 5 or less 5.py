# lst=[7,8,9,1,2,3]
#
# for num in lst:
#     if num>5:
#         print(num+1)
#     else:
#         print(num-1)

lst=[7,8,9,1,2,3]

re=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(re)