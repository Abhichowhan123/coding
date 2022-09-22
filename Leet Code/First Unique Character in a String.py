s = "leetcode"
A = {}
for i in s:
    if i in A:
        A[i]+=1
    else:
        A[i] = 0
for i in range(len(s)):
    if A[s[i]]==0:
        print(i)
        break
print(-1)