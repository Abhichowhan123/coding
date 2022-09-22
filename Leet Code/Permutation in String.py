s1 = "ab"
s2 = "eidbaooo"
s1 = "".join(sorted(s1))
n = len(s1)
if len(s2)<len(s1):
    print(False)
i= 0
while n!=len(s2)+1:
    a = "".join(sorted(s2[i:n]))
    if a == s1:
        print(True)
    i+=1
    n+=1



# s1 = "ab"
# s2 = "eidboaoo"
# if len(s1) > len(s2):
#     print("false")
# A = [0]*26
# B = [0]*26
# for i in range(len(s1)):
#     A[ord(s1[i])-97] +=1
#     B[ord(s2[i])-97] +=1
# if A == B:
#     print("true")
# for i in range(len(s1),len(s2)):
#     B[ord(s2[i-len(s1)])-97]-=1
#     B[ord(s2[i]) - 97] += 1
#     if A == B:
#         print("true")
# print("false")


# s1 = "ab"
# s2 = "eidboaoo"
# A = {}
# e = 0
# for i in s1:
#     if i in A:
#         A[i]+=1
#     else:
#         A[i]=1
# for j in range(len(s2)):
#     r =0
#     B = {}
#     i = j
#     while r<len(s1):
#         if i!=len(s2):
#             if i in B:B[s2[i]] +=1
#             else:B[s2[i]] = 1
#             i+=1
#         r+=1
#
#     if A==B:
#         e=1
#         print("true")
# if e==0:
#     print("false")