
"""
def check(arr):
    n = len(arr)
    arr2 = [0] * (n)
    for i in range(0, n):
        arr2[arr[i] - 1] = i + 1
    z = 0
    for i in range(n):
        if arr[i] != arr2[i]:
            z = 1
            break
    if z == 0:
        return "ambiguous"
    else:
        return "not ambiguous"

while (True):
    t = int(input())
    if t == 0:
        break
    x = list(map(int, input().split()))
    print(check(x))

"""