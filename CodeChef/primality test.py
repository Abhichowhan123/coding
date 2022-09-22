"""A = [2,3,5,7,9]
flag = 0
for i in range(int(input())):
    n = int(input())
    for j in range(len(A)):
        if (n % A[j] == 0):
            flag = 1
            break
        elif (flag == 1):
            print("no")
            break
        else:
            print("yes")
            break"""

t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for j in range(1, n):
        if n % j == 0:
            count += 1
    if count == 1:
        print("yes")
    else:
        print("no")