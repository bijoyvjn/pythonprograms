
def search():
    list = [11, 2, 3, 4, 5, 8, 9, 6, 7]
    num = int(input("enter the number"))
    flag=0
    for i in list:
        if (num == i):
            flag=1
            break
    if (flag > 0):
        print("search found")
    else:
        print("not found")
search()
