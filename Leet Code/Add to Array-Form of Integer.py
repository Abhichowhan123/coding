num = [2,7,4]
A  =[ ]
k = 181
a= ""
for i in num:
    i = str(i)
    a+=i
a =str(int(a)+k)
for j in a:
    j = int(j)
    A.append(j)
print(A)