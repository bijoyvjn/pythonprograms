def swap(fu):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fu(n1,n2)
    return wrapper

@swap
def div(n1,n2):
    return n1/n2

print(div(5,10))

@swap
def sub(n3,n4):
    return n3-n4

print(div(5,10))
