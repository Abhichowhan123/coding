# import collections
# s = "bbaaacbd"
# k = 3
# A={}
# for i in s:
#     if i not in A:
#         A[i]=1
#     else:
#         A[i]+=1
# Max = 0
# freq,Str = {},""
# for j in s:
#     if A[j]>=k:
#         Str+=j
#         if j in freq:
#             freq[j]+=1
#         else:
#             freq[j] = 1
#         for o,p in freq.items():
#             if p<k:
#                 Max =0
#             else:
#                 Max  =max(Max,len(Str))
#     else:
#         Str= ""
#         freq  ={}
# print(Max)
s = "ababacb"
k = 3
A= {}
maxx = -999
a = ''
for i in range(len(s)):
    if A[s[i]]>=k:
        a+=s[i]
        maxx = max(maxx,len(a))
    else:
        a = ''
print(maxx)