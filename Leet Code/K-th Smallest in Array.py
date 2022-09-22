n = int(input())
A = list(map(int,input().split()))
k= int(input())
# A = [7,10,4,3,20,15]
# n= 6
# k = 4
min = 99999999
max = 0
for i in range(len(A)):
    if A[i]<min:
        min=A[i]
    elif A[i]>max:
        max= A[i]
def fun(x):
    cou = 0
    for j in range(len(A)):
        if A[j] <= x:
            cou+=1
    return cou

l = min
h = max
while l<=h:
    m = (l+h)//2
    count = fun(m)
    if count<k:
        l =m+1
    else:
        count1 = fun(m-1)
        if count1<k:
            print(m)
            break
        else:
            h = m-1