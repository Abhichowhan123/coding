
# A = "ANSHUMAN"
# B = "ANTIHUMAN"
# dic1 = {}
# dic2 = {}
# for i in A:
#     if i in  dic1:
#         dic1[i]+=1
#     else:
#         dic1[i] = 1
# for i in B:
#     if i in  dic2:
#         dic2[i]+=1
#     else:
#         dic2[i] = 1
# count = 0
#
# for j,k in dic1.items():
#     if j in dic2 and dic2[j]==k:
#         dic1[j] = 0
#         dic2[j] = 0
# r = 0
# for j,k in dic2.items():
#     r+=k
# print(r)
#
# import json
# # A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
# your_json = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
# parsed = json.loads(your_json)
# print(json.dumps(parsed, indent=4, sort_keys=True))

import json
print(json.dumps({A:"B",C:{D:"E",F:{G:"H",I:"J"}}}, indent=4))






# def reverseWords(s):
#     r = ""
#     q = ""
#     for i in s:
#         if i==" ":
#             r+=q[::-1]+" "
#             q = ""
#         else:
#             q+=i
#
#     r = q+""+r[::-1]
#     return r
# s = "i like this program very much"
# print(reverseWords(s))















# a = [3,4,5,3,100,1,83,54,23,20]
# s = 0
# for i in range(len(a)):
#     s+=a[i]
# s= s//2
# A ={}
# def total(e,w):
#     if e==0:
#         print("hello")
#         return
#     if e<0:
#         return
#     for i in range(w,len(a)//2):
#         total(e-a[i],i+1)
# total(s,0)
# a = str(input())
# b = str(input())
# s = ""
# F = ""
# a+=" "
# for i in range(len(a)):
#     if a[i]!=" ":
#         s+=a[i]
#     elif a[i]==" ":
#
#         if s==b:
#             s = ""
#             pass
#         else:
#             F = F+" "+s
#             s=""
# print(F)




# u = int(input())
# A = list(map(int,input().split()))
# n =, int(input())
# # A  = [2,7,11,15 ]
# # n = 9
# dic = {}
# for i in range(len(A)):
#     if n-A[i]in dic:
#         print(dic[n-A[i]],i+1)
#         break
#     if A[i] not in dic:
#         dic[A[i]] = i+1


# # for i in range(int(input())):
# def t(a):
#     c = 0
#     while a != 0:
#         b = a % 10
#         c += b
#         a = a // 10
#     return c
# a =1100
# g = a
# c = 0
# while a!= 0:
#     b = a%10
#     c+=b
#     a = a//10
# f = 0
# while 1:
#     if f>c:
#         break
#     g = g-1
#     f = t(g)
# print(g)9kk-
# print(9%4)




# for i in range(int(input())):
#     a = int(input())
#     b = 0
#     c =4
#     s =1
#     while a!=0:
#         if c ==0:
#             c=4
#             s+=1
#         d= c*s
#         b+=d
#         a-=1
#         c-=1


# # a = "a12.3bc34d8ef34"
# a = "a1b01c001"
# prev = 0
# dic={}
# for  i in range(len(a)):
#     if a[i]==".":
#         pass
#     elif not a[i].isdigit():
#         w =a[prev+1:i]
#         if w not in dic and w !="":
#             e = int(w)
#             dic[e] = 0
#         prev = i
# print(len(dic))
# def TreeConstructor(strArr):
#     from collections import Counter
#     parent = []
#     child = []
#
#     for i in strArr:
#         child.append(int(i[1]))
#         parent.append(int(i[3]))
#     # each parent node have at most 2 children
#     for k,v in Counter(parent).items():
#         if v > 2:
#             return False
#     # each node is unique
#     for k,v in Counter(child).items():
#         if v > 1:
#             return False
#     return True
#
# print (TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))      # True
# print (TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"] ))      # False


# S  =["01111", "01101", "00011", "11110"]
# dic = {}
# for i in range(len(S)):
#     for j in range(len(S[i])):
#         dic[(i, j)] = int(S[i][j])
#
# hole_count = 0
# hole = set()
# checked = set()
# flag = True
#
# for i in range(len(S)):
#     for j in range(len(S[i])):
#         stack = [(i, j)]
#         while stack:
#             A  =stack.pop()
#             if A not in checked:
#                 checked.add(A)
#                 if dic[A] == 0 and A not in hole:
#                     hole.add(A)
#                     if flag == True:
#                         hole_count += 1
#                         flag = False
#                     if A[0] - 1 >= 0 and (A[0] - 1, A[1]) not in checked:
#                         stack.append((A[0] - 1, A[1]))
#                     if A[0] + 1 < len(S) and (A[0] + 1, A[1]) not in checked:
#                         stack.append((A[0] + 1, A[1]))
#                     if A[1] - 1 >= 0 and (A[0], A[1] - 1) not in checked:
#                         stack.append((A[0], A[1] - 1))
#                     if A[1] + 1 < len(S[A[0]]) and (A[0], A[1] + 1) not in checked:
#                         stack.append((A[0], A[1] + 1))
#         flag = True
#
# print(hole_count)



# """
# # s = "abccdefghi"
# # m= 0
# # dic = {}
# # for i in range(len(s)):
# #     if s[i] in dic:
# #         if dic[s[i]]+1!= i:
# #             m = max(m,abs(i-dic[s[i]])-1)
# #     dic[s[i]]  =i
# # print(m)
#
# """



# A =  [9,5,6,9,9,7,9]
# dic= {}
# Min = 9999999
#
# for i in range(len(A)):
#     if A[i] in dic:
#         Min = min(Min,i-dic[A[i]])
#
#     dic[A[i]]  =i
# print(Min+1)

# def R(count,w):
#     w-=2
#     if w==0:
#         return count,w
#     else:
#         w+=1
#     return count+1,w
# count = 0
# x=2
# y=4
# w = x+y
# while w!=0:
#     count,w = R(count,w)
# print(count)




# N = 3
# M = 1
# Q = [2]
# A = {}
# for j in Q:
#     A[j]=1
# B = {1:0}
# def rec(i,count):
#     if i==N:
#         return 1
#     if i>N:
#         return 0
#     if i not in A:
#         count+=rec(i+1,count)
#         count+=rec(i+2,count)
#         count+=rec(i+3,count)
# count = 0
# rec(0,count)
# print(B[1])
#
#


# N = 3
# S = "BAC"
# dic = {"A":1,"E":1,"I":1,"O":1,"U":1}
# B = []
# def cobbination(j,T):
#     if j ==len(S):
#         if len(T)>=N and T not in B:
#             B.append(T)
#         return
#     if S[j] not in dic:
#         cobbination(j+1,T+" "+S[j])
#     else:
#         cobbination(j + 1, T + S[j])
#     cobbination(j+1,T+S[j])
# i = 0
#
# T = ""
# cobbination(i,T)
# print(B)
