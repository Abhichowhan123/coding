import math

for i in range(int(input("no of test case"))):
    n = int(input("\nno for all factor"))
    f = int(math.sqrt(n))
    for  j in range(1,f+1):
        if n%j==0:
            if j*j ==n:
                print(j)
            else:
                print(j,n//j,end= " ")