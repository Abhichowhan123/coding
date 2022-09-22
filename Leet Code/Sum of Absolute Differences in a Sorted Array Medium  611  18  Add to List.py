num = [1,4,6,8,10]
A= []
B = []
a = 0
for i in range(len(num)):
    a+=num[i]
    A.append(a)
for j in range(len(num)):
    b = 0
    if j==0:
        b = A[len(num)-1]-(len(num)*num[j])
        B.append(b)
    else:
        w = len(num) - j - 1
        b = abs(abs((A[len(num)-1]-A[j])-(w*num[j])) + abs((j*num[j])-(A[j-1])))
        B.append(b)
print(B)