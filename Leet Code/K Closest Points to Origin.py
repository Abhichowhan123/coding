# A = [[1,3],[-2,2]]
# B = []
# C = []
# k=1
# class distence:
#     def __init__(self,dist,value1,value2):
#         self.dist = dist
#         self.value1 = value1
#         self.value2 = value2
# for i,j in A:
#     a = (i**2)+(j**2)
#     obj = distence(a,i,j)
#     c = [obj.dist,obj.value1,obj.value2]
#     B.append(c)
# c = sorted(B,key=lambda x: x[0])
# for i in range(k):
#     s = [c[i][1],c[i][2]]
#     C.append(s)
# print(C)
import heapq

points = [[1,3],[-2,2]]
k = 1
A = []
heapq.heapify(A)
for i in range(len(points)):
    a = -( (points[i][0])**2 +(points[i][1])**2)
    b = [a,points[i][0],points[i][1]]
    if len(A)<k:
        heapq.heappush(A,b)
    else:
        heapq.heappushpop(A, b)
B = []
for i in range(k):
    B.append([A[i][1],A[i][2]])
print(B)

