
def search(lis,a,d):
    c = 0
    for c in range(a):
        if lis[c]==d:
            print("found the no at",c)
            return 0

    print("not found")

lis = []
a = int(input("total no"))  #taking total no
for i in range(a):          #loop for list
    b = int (input(":-"))
    lis.append(b)

d = int (input("enter the no you want to search "))

search(lis,a,d)


