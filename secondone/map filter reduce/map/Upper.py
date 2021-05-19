lst=['bijoy','arun']

# def upp(name):
#     return name.upper()

# upper=map(upp,lst)    it is not a list so convert it into list
# print(upper)

# upper=list(map(upp,lst))      now it is list but delete the def function and make it in lambda
# print(upper)

upper=list(map(lambda name:name.upper(),lst))
print(upper)