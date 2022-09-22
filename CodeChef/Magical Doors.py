#
# def change(A):
#     for k in range(0,len(A)):
#         if A[k]=="0":
#             A[k]="1"
#         else:
#             A[k]= "0"
#     return 1
# for i in range(int(input())):
#     A = list(input())
#     count = 0
#     p = 0
#     for j in range(len(A)):
#         if A[j]=="0":
#             p+=change(A)
#     print(p)



for i in range(int(input())):
    A = list(input())
    p = "1"
    count = 0
    for j in range(len(A)):
        if p!=A[j]:
            p = A[j]
            count+=1
    print(count)
















