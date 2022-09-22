n=  3
a=1
b=1
for i in range(n-1):
    t =a
    a = a+b
    b = t
print(a)




# n = 38
# A = []
# def climbing(n,temp):
#     if temp == n:
#         A.append(1)
#         return
#     if temp>n:
#         return
#     climbing(n,temp+1)
#     climbing(n, temp + 2)
#
# climbing(n,0)
# print(len(A))