# for i in range(int(input())):
#     a = int(input())
#     A = []
#     for j in range(10000):
#         if j%3==0:
#             if j%9!=0:
#                 if j%2!=0:
#                     A.append(j)
#     for k in range(len(A)):
#         if a==1:
#             if A[k]<10:
#                 print(A[k])
#                 break
#         if a==2:
#             if 10<A[k]<100:
#                 print(A[k])
#                 break
#         if a==3:
#             if 100<A[k]<1000:
#                 print(A[k])
#                 break
#         if a==4:
#             if 1000<A[k]<10000:
#                 print(A[k])
#                 break

for i in range(int(input())):
    a = int(input())
    if a ==1:
        print("3")
    elif a==2:
        print("33")
    elif a==3:
        print("303")
    else:
        w = "0"*(a-2)
        print("3"+w+"3")