s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
wor = { }
b = 0
for i in wordDict:
    wor[i] = 0
def word_brek(b,a,c):
    if len(s)== c:
        b+=1
        return
    st = ""
    for i in range(a,len(s)):
        st+=s[i]
        if st in wor:
            c+=len(st)
            word_brek(b,i+1,c)
word_brek(b,0,0)
if b>=1:
    print("true")
else:
    print("false")

