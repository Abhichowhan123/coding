s =  "abccba"
a = "ba"
check = ""
stack  = []
for i in s:
    if i =="c":
        n=2
        while n!=0:
            if len(stack)!=0:
                check+=stack.pop()
            n-=1
        if check!=a:
            print(False)
        else:
            check=""
    else:
        stack.append(i)
if len(stack)==0:
    print(True)
else:
    print(False)
