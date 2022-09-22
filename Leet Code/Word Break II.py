s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
wor = {}
for i in wordDict:
    wor[i]  =0

A  = []
B = []
def Word_Break(b,A):
    if len(s)==b:
        B.append(' '.join(A))
        return
    st = ""
    for i in range(b,len(s)):
        st+=s[i]
        if st in wor:
            A.append(st)
            Word_Break(i+1,A)
            A.pop()
Word_Break(0,A)
print(B)