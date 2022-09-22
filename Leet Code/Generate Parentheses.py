n = 3
A = []
def pp(a,l,r):
    if l<n:
        pp(a+"(",l+1,r)
    if l>r:
        pp(a+")",l,r+1)
    if l==n and r==n:
        A.append(a)
    return A
pp(a= "",l=0,r=0)
print(A)


# n=3
# S = [0]*(2*n)
# A = []
# def pp(l,r,i):
#     if i == 2*n:
#         A.append(S)
#         return
#     if l==r :
#         S[i]="("
#         pp(l+1,r,i+1)
#     if l>r:
#         if l==n:
#             S[i]=")"
#             pp(l,r+1,i+1)
#         else:
#             S[i] = "("
#             pp(l+1,r,i+1)
#             S[i] = ")"
#             pp(l,r+1,i+1)
# pp(l=0,r=0,i=0)