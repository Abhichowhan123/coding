
n = 3
top = 0
down = n-1
left = 0
right = n-1
diration = 0
A  =[[0]*n for _ in range(n)]
a=1
while top<=down and left<=right:
    if diration==0:
        for i in range(left,right+1):
            A[top][i] = a
            a+=1
        top+=1
    elif diration==1:
        for j in range(top,down+1):
            A[j][right]=a
            a+=1
        right-=1
    elif diration==2:
        for k in range(right,left-1,-1):
            A[down][k] = a
            a+=1
        down-=1
    elif diration ==3:
        for l in range(down,top-1,-1):
            A[l][left]=a
            a+=1
        left+=1
    diration = (1+diration)%4
print(A)