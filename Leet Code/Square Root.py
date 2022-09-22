for i in range (int(input())):
    n = int(input())
    l = 0
    h = n
    while(l<=h):
        m = (l+h)//2
        if (m*m)>n:
            h = m+1
        else:
            if n<((m+1)*(m+1)):
                print(m)
                break
            if n==((m+1)*(m+1)):
                print(m+1)
                break
            else:
                l=m+1
