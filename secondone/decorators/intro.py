# If we use a decorator we can build a fuction one and we can reuse that in different times
# in the language "we can decorate a function"

#-------------------------------------------------------------------------------------------
# Here we need to explain that every time the program need to reduce the lowest number from the highest number.

# def sub(n1,n2):
#     if n1<n2:
#         (n1,n2)=(n2,n1)
#
#     return n1-n2
#
# result=sub(5,10)
# print(result)

#------------------------------------------------------------------------
# if we use a decorator

def dec_swap(f):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return f(n1,n2)
    return wrapper


@dec_swap
def sub(n1,n2):
    return n1-n2

result=sub(2,10)
print(result)