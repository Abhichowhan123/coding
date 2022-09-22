A = []
n =30
for i in range(1,int((n/2)/2)):
    if n%i==0:
        if i*i==n:
            A.append(i)
            break
        else:
            A.append(i)
            A.append(int(n/i))
print(A)