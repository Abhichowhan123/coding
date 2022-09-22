matrix = [["0"]]
def histogram(arr):
    i = Max  =  0
    while i!=len(arr):
        r = l = i
        left = right = 0
        while l!=-1  :
            if arr[i]==0:break
            if l!=-1  :
                if arr[l]>=arr[i]:
                    left+=arr[i]
                    l -= 1
                else:break
        while r!=len(arr):
            if arr[i] == 0: break
            if r!=len(arr) :
                if arr[r]>=arr[i]:
                    right+=arr[i]
                    r+=1
                else:break
        Max = max(Max,(left+right)-arr[i])
        i += 1
    return (Max)
result = 0
A=[0]*(len(matrix[0]))
for i in matrix:
    for j in range(len(matrix[0])):
        if int(i[j])==0:
            A[j] =0
        else:
            A[j] +=int(i[j])
    result = max(result,histogram(A))
print(result)