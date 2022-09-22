height = [1,1]
A  = []
i = 0
j = len(height)-1
l = len(height)-1
while i!=j:
    if height[i]<height[j]:
        A.append(l*height[i])
        i+=1
    else:
        A.append(l*height[j])
        j-=1
    l-=1
print(max(A))