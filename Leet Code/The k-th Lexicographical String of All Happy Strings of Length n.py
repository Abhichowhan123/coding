n = 3
k = 9
s= ['a', 'b', 'c']
A = []
def  Lexicographical_String(st,s,n,A):
    if len(st)==n:
        A.append(st)
        return
    else:
        for j in s:
            if st[-1]!=j:
                Lexicographical_String(st+j,s,n,A)
st = ""
for i in s:
    Lexicographical_String(i,s,n,A)
if len(A)<k:
    print("")
else:
    print(A[k-1])