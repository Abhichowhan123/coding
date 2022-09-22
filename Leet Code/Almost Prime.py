import math

total_no = 1000001
Array = [0]*(total_no+1)
thp = [0]*(total_no+1)
Array[0] = Array[1] = -1
sqrt_total_no = int(math.sqrt(total_no))
for i in range(2,total_no+1):
    count = 0
    if Array[i]==0:
        j = i
        for j in range(2,total_no+1):
            if j%i==0:
                Array[j] +=1
            if Array[j]==2:
                count+=1
            if thp[j]<count:
                thp[j] = count
for k in range(int(input())):
    n  = int(input())
    print(thp[n])