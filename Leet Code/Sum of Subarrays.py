a = []
b = 0

for i in range(0,len(a)):
    b += (i+1)*(len(a)-i)*a[i]
print(b)