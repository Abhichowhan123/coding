def count(w):
    i = 0
    for k in range(len(w)):
        if w[k] == 4:
            i+=1
    print(i)
    return 1


def check(j):
    q = []
    while j != 0:
        b = int(j % 10)
        j = int(j / 10)
        q.append(b)
    count(q)
    return 1


if __name__ == "__main__":
    a = []
    b = int(input())        #total no want to enter
    for i in range (b):
        c = int(input())    #no for to checks four
        a.append(c)
    for j in range(len(a)):
        check(a[j])

