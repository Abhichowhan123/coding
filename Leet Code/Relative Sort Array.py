arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
# [22,28,8,6,17,44]
A = []

for i in arr2:
    for j in range(arr1.count(i)):
        A.append(i)

for k in sorted(arr1):
    if k not in arr2:
        A.append(k)
print(A)