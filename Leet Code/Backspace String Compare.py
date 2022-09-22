s = "a#c"
t = "b"
S =[]
T =[]
for i in range(len(s)):
    if s[i]=="#":
        if len(S)!=0:
            S.pop()
    else:
        S.append(s[i])
for j in range(len(t)):
    if t[j]=="#":
        if len(T)!=0:
            T.pop()
    else:
        T.append(t[j])
if "".join(S) == "".join(T):
    print(True)
else:
    print(False)