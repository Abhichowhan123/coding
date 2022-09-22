s="aabb"
A = []
B = []
def palindrome(s,i,A,B):
    if i==len(s):
        B.append(A[:])
        return
    for j in range(i,len(s)):
        st = s[i:j+1]
        stt = "".join(st[::-1])
        if stt==st:
            A.append(st)
            palindrome(s,j+1,A,B)
            A.pop()
palindrome(s,0,A,B)
print(B)