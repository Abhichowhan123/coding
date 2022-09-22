matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
top = 0
down = len(matrix)-1
left = 0
right = len(matrix[0])-1

diration = 0
A = []
while top<=down and left<=right:
    if diration==0:
        for i in range(left,right+1):
            A.append(matrix[top][i])
        top+=1
    elif diration==1:
        for j in range(top,down+1):
            A.append(matrix[j][right])
        right-=1
    elif diration==2:
        for k in range(right,left-1,-1):
            A.append(matrix[down][k])
        down-=1
    elif diration ==3:
        for l in range(down,top-1,-1):
            A.append(matrix[l][left])
        left+=1
    diration = (1+diration)%4
print(A)