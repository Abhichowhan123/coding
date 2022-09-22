s = "(((((*)))**"
openS =[]
star = []
for i in range(len(s)):
    if s[i]=="(":
        openS.append(i)
    elif s[i]== "*":
        star.append(i)
    else:
        if s[i]==")":
            if len(openS)!=0:
                openS.pop()
            elif len(star)!=0:
                star.pop()
            else:
                print(False)
if len(openS)!=0:
    for j in range(len(openS)-1,-1,-1):
        if len(star)!=0:
            if openS[j] < star[-1]:
                openS.pop()
                star.pop()
            else:
                print(False)
        else:
            print(False)
if len(openS)==0:
    print(True)
else:
    print(False)