A = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}

# def most(root):
#     if root:
#         if root.val in A:
#             A[root.val]+=1
#         else:
#             A[root.val] = 1
#         most(root.left)
#         most(root.right)
#
# root = [1,0,2,2]
# most(root)
A=sorted(A.items(),key= lambda x:x[1],reverse=True)
print(A)
B = []
a= -3333
for i,j in A:
    if j>=a:
        B.append(j)
        a = j
    else:
        break
print(B)
