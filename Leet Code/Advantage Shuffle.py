nums1 = [2,7,11,15]
nums2 = [1,10,4,11]
A= []
for i,j in enumerate(nums2):
    A.append((j,i))
A  =sorted(A,key=lambda x:x[0],reverse=True)
a = sorted(nums1,reverse=True)
B = [None]*len(nums2)
for i in A:
    if a[0]>i[0]:
        B[i[1]]  = a[0]
        del a[0]
for k in range(len(B)):
    if B[k]==None:
        B[k]=a[0]
        del a[0]
print(B)