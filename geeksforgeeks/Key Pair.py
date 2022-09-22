
n = 3
x = 468
arr = [335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605,
       903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812,
       323, 334]
A = {}
for i in arr:
    if x-i in A:
        print("Yes")
    A[i]  = 1
print("No")
# for i in range(len(arr)):
#     if arr[i] in A:
#         A[arr[i]] +=1
#     else:
#         A[arr[i]] = 1
# for j in A:
#     if j == x-j and A[j]>1:
#         print("Yes")
#         break
#     elif x-j in A and j != x-j:
#         print("Yes")
#         break

