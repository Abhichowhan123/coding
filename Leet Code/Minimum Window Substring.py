import collections
s = "cabwefgewcwaefgcf"
t = "cae"
A,need = {},0
for i in t:
    if i in A:
        A[i]+=1
        # need+=1
    else:
        A[i]=1
        need+=1
check = {}
result , have = 999999999,0
queue ,R,F= collections.deque(),"",""
for j in s:
    if j in A:
        if j in check:
            check[j]+=1
        else:
            check[j]=1
        if check[j]==A[j]:
            have+=1
    queue.append(j)
    if have==need:
        while have==need:
            if len(queue)<result:
                F = "".join(queue)
            result = min(result, (len(queue)))
            w =  queue[0]
            if w in A:
                check[w] -= 1
                if check[w]<A[w]:
                    have-=1
            R = queue.popleft()
queue.appendleft(R)
U = ""
for k in range(len(queue)-1,-1,-1):
    U = queue[k]
    if U in A:
        break
    else:
        queue.pop()
G = "".join(queue)
if result!=999999999:
    if len(F)<=len(G):
        print(F)
    else:
        print(G)
else:
    print("")


# if R in A:
#     if have!=need:
#         check[R]+=1
#         if check[R]==A[R]:
#             if result != 999999999:
#                 print(R + "".join(queue))
#             else:
#                 print("")
# else:
#     if result!=999999999:
#         print("".join(queue))
#     else:
#         print("")