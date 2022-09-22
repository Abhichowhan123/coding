s = "weallloveyou"
k=7
v = ['a', 'e', 'i', 'o', 'u']
count = 0
for  i in range(k):
    if s[i] in v:
        count+=1
cv = count
a =b = 0
r= k-1
while r<len(s)-1:
    if s[a] in v:
        count-=1
    a+=1
    r+=1
    if s[r] in v:
        count+=1
    if count>b:
        b= count
print (max(cv,b))


# s = "aeiou"
# k=3
# v = {'a', 'e', 'i', 'o', 'u'}
# y = s[:k]
# count = sum(1 for char in y if char in v)
# m = count
# for i in range(k, len(s)):
#     h = i - k
#     a, t = s[h], s[i]
#     if a in v:
#         count -= 1
#     if t in v:
#         count += 1
#     m = max(m, count)
# print(m)


# n = len(s)
# i,j = 0,0
# d = {'a':0,'e':0,'i':0,'o':0,'u':0}
# res = 0
# while j<n:
#     if s[j] in d:
#         d[s[j]]+=1
#     if j-i+1<k:
#         j+=1
#     elif j-i+1==k:
#         res = max(res,sum(d.values()))
#         if s[i] in d:
#             d[s[i]]-=1
#         i+=1
#         j+=1
# print(res)
#

# for i in range(len(s)):
#     w = k
#     count = 0
#     for g in range(i,w):
#         if w==0:
#             break
#         else:
#             if s[g] in vo:
#                 count+=1
#         w -= 1
#     if A < count:
#         A = count
# print(A)