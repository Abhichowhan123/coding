A = [2010,2015,2016,2017,2019]
for i in range(int(input())):
    n = int(input())
    count=0
    for j in range(len(A)):
        if (n==A[j]):
            print("HOSTED")
            count+=1
    if(count==0):
        print("NOT HOSTED")