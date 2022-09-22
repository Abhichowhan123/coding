arr= [1, 2, 3, 4, 5]
def subArrayExists( arr, n):
    A = {}
    a = 0
    A[a] = 1
    for i in range(len(arr)):
        a += arr[i]
        if a in A:
            return "Yes"
        A[a] = 1

    return "No"
n = 5
print(subArrayExists( arr, n))