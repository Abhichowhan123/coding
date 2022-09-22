list = []
print("Enter number of elements : ")
n = int(input())
for i in range(0,n):
    b=int(input("next no :"))
    list.append(b)
print(list)

def count(list):
    even= 0
    odd = 0
    for i in list:
        if i%2==0:
            even=even+1
        else:
            odd = odd + 1
    return even,odd


even,odd = count(list)
print("even : {} and odd : {} ".format(even,odd))
