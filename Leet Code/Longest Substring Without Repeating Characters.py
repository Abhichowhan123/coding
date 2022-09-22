s =  "abcabcbb"
A=[]
count = 0
for i in s:
    if i not in A:
        A.append(i)
    else:
        a = A.index(i)
        del A[0:a+1]
        A.append(i)
    count = max(count, len(A))
print(count)
