low = 234
high =2314
A = "123456789"
B =[]
a = 2
e = 8
for i in range(len(A)):
    for j in range(e):
        b=a
        q = j
        w =''
        while b>0:
            w+=A[q]
            b-=1
            q+=1
        B.append(int(w))
    e-=1
    a+=1

C = []
for j in range(len(B)):
    if B[j]>=low and B[j]<=high:
        C.append(B[j])
print(C)
