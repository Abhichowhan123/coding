# import math
# a = 20
# A = [0]*(a+1)
# A[0]=A[1]= -1
# b = int(math.sqrt(len(A)))
# count = 0
# for i in range(b+1):
#     if A[i]== 0:
#         count+=1
#         for j in range(i+1,len(A)):
#             if A[j] == 0:
#                 if j%i==0:
#                     A[j] = -1
#
# print(A)
# print(count)
















import math
w = 100
spf = [0]*(w+1)
A = [True]*(w+1)
f = int(math.sqrt(w))
A[0] = A[1]  =False
for l in range(2,f+1):
    if A[l]==True:
        for j in range(l*l,w+1):
            if j%l==0:
                A[j] = False
count = 0
for k in range(len(A)):
    if A[k]==True:
        count+=1
        spf[k] = count
    else:
        spf[k] = count
print(count)