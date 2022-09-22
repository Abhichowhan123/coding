a = [1,3,0,2]

for i in range(len(a)):
    if a[i]>=0:
        ind= a[i]
        val = i
        while ind!=i:
            temp = a[ind]
            a[ind] = -(val+1)
            val = ind
            ind = temp
        a[ind] = -(val+1)
for j in range (len(a)):
    a[j] = -1 * a[j]-1
print(a)