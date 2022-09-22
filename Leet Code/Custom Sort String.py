order = "cbafg"
s = "abcd"
# order = "kqep"
# s = "pekeq"
a = ""
for i in order:
    for j in range(s.count(i)):
        a+=i
for k in s:
    if k not in order:
        a+=k
print(a)

# a  =list(order)
# b = list(s)
# A = [28]*26
# B = {}
# for i in range(len(a)):
#     A[ord(a[i]) - ord("a")] = i
# for j in range(len(b)):
#     B[b[j]] =A[ord(b[j])-ord("a")]
# r =sorted(B.items(),key=lambda x:x[1])
# f= ""
# for k ,l in r:
#     f+=k
# print(f)