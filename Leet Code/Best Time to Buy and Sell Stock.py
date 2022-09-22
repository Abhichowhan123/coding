prices =[7,1,5,3,6,4]
pre  = []
suf = [None]*len(prices)
count = 0
ma = -999999999
mi = 99999999
for i in range(len(prices)):
    if mi >prices[i]:
        mi =  prices[i]
        pre.append(mi)
    else:
        pre.append(mi)
for j in range(len(prices)-1,-1,-1):
    if ma <prices[j]:
        ma = prices[j]
        suf[j] = ma
    else:
        suf[j] = ma
a = b= 0
while a<len(prices):
    if suf[a]-pre[a]>count:
        count  = suf[a]-pre[a]
    a+=1

print(count)



# ma = 0
# for i in range(len(prices)-1,0,-1):
#     for j in range(i-1,-1,-1):
#         if prices[i]-prices[j]>ma:
#             ma = prices[i]-prices[j]
# print(ma)
#
# A = [7,6,4,3,1]
# b = min(A)
# c = 0
# for i in range(len(A)):
#     if A[i]==b:
#         c = i
# ma = 0
# for j in range(c,len(A)):
#     if ma<A[j]:
#         ma =A[j]
# d = ma-b
# if d<=0:
#     print("0")
# else:
#     print(d)
#
