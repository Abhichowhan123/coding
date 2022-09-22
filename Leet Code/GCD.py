# GCD 1 example
for k in range(int(input())):
    w,x=map(int,input().split())
    a =max(w,x)
    b = min(w,x)
    if (b==0):
        print(a)
        break
    while(a%b!=0):
        tem = a
        a=b
        b=tem%b
    print(b)

# # GCD 2 example
# for k in range(int(input())):
#     w,x=map(int,input().split())
#     a =max(w,x)
#     b = min(w,x)
#     for i in range(int(b/2)):
#         if a % b != 0:
#             b ,a= a%b,b
#         if a % b==0:
#             print(b)
#             break