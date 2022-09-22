arr = []
a = int (input())
for i in range(a):
    b = int(input())
    arr.append(b)
for j in range(len(arr)):
    if arr[j]< 10:
        print("Thanks for helping Chef!")
    else:
        print("-1")