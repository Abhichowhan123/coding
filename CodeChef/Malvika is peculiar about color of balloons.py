for i in range(int(input())):
    n = list(input())
    w = n.count("a")
    x = n.count("b")
    if w<=x:
        print(w)
    elif x<w:
        print(x)