s = "101023"
A = []

def RIA(i,dot,b):

    if i==len(s) and dot == 4:
        A.append(b[:-1])
        return
    if dot >4:
        return
    for j in range(i,len(s)):
        if int(s[i:j+1]) <=255 and (len(s[i:j+1])==1 or s[i]!="0"):
            RIA(j+1,dot+1,b+s[i:j+1]+".")
if len(s)<=12:
    RIA(0,0,"")
    print(A)
else:
    print(A)