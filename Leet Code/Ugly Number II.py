# import heapq
# n = 11
# num = [2,3,5]
# dic = {2:0,3:0,5:0}
# B =[1]
# def isprime(n):
#     import math
#     count = 0
#     f = int(math.sqrt(n))
#     for i in range (2,f+1):
#         if n%i==0:
#             count+=1
#     if count==0:
#        return True
#     else:
#         return False
# while len(B)!=n:
#     A = []
#     heapq.heapify(A)
#     heapq.heappush(A,[2* isprime(dic[2]+1),2])
#     heapq.heappush(A, [3 * (dic[3] + 1),3])
#     heapq.heappush(A, [5 * (dic[5] + 1),5])
#     d = heapq.heappop(A)
#     if d[0] not in B:
#         B.append(d[0])
#     dic[d[1]]+=1
# print(B[len(B)-1])
class Solution:
    # First few ugly numbers
    ugly = [1, 2, 3, 4, 5, 6, 8, 9, 10]

    def nthUglyNumber(self, n: int) -> int:
        ugly = self.ugly
        if n < len(ugly):
            return ugly[n - 1]

        for i in range(len(ugly), n):
            biggest = ugly[-1]
            mul2 = 2 * ugly[bisect_right(ugly, biggest // 2)]
            mul3 = 3 * ugly[bisect_right(ugly, biggest // 3)]
            mul5 = 5 * ugly[bisect_right(ugly, biggest // 5)]
            ugly.append(min(mul2, mul3, mul5))

        return ugly[n - 1]
