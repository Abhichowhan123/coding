def fact(e):
     f = k = 1
     while k <= e:
         f = f*k
         k +=1
     print("\n",f)
     return 1

a = []
if __name__ == '__main__':
    b= int(input())            #total no want enter
    for i in range (b):
        c = int(input())
        a.append(c)
    for j in range(len(a)):
        d = fact(a[j])