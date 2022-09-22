num = "10001"
k = 4
stack  = []
if len(num)==k:
    print("0")
else:
    for i in num:
        if i != "0" and len(stack) == 0:
            stack.append(i)
        else:
            if k > 0 and stack and stack[-1] < i:
                if i == "0" and len(stack) == 0:
                    continue
                else:
                    stack.append(i)
            else:
                while k > 0 and stack and stack[-1] > i:
                    stack.pop()
                    k-=1
                if i=="0" and len(stack)==0:
                    continue
                else:
                    stack.append(i)
    d = "".join(stack)
    if num==d :
        print(d[:(len(num))-k])
    else:
        if k!=0:
            if len(d)==0:
                print("0")
            elif len(d)<=k or len(d)>=k :
                if len(d[:len(d)-k])==0:
                    print("0")
                else:
                    print(d[:len(d)-k])
        else:
            print(d)
