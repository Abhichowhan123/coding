s = "14-3/2"
s+="@"
st = []
cur =""
n = len(s)
i,oper = 0,"+"
while n!=0:
    if s[i]!="+" and s[i]!="-" and s[i]!="*" and s[i]!="/" and s[i]!="@" and s[i]!=" ":
        cur+=s[i]
    else:
        if s[i]!=" ":
            if oper=="+":
                st.append(cur)
            elif oper=="-":
                st.append(oper+cur)
            elif oper=="*":
                st.append(str(int(st.pop()) * int(cur)))
            elif oper == "/":
                st.append(str(int(int(st.pop()) / int(cur))))
            cur = ""
            oper = s[i]
    n-=1
    i+=1
A =  0
for i in st:
    A+=int(i)
print(A)