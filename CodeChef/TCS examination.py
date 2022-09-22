for i in range(int(input())):
    DSA1,TOC1,DM1 = list(map(int,input().split()))
    DSA2, TOC2, DM2 = list(map(int, input().split()))

    if DSA1+TOC1+DM1> DSA2+TOC2+DM2:
        print("DRAGON")
    elif DSA1+TOC1+DM1< DSA2+TOC2+DM2:
        print("SLOTH")
    if DSA1 + TOC1 + DM1 == DSA2 + TOC2 + DM2:
        if DSA1>DSA2:
            print("DRAGON")
        elif DSA1 < DSA2:
            print("SLOTH")
        if DSA1 == DSA2:
            if TOC1 > TOC2:
                print("DRAGON")
            elif TOC1 < TOC2:
                print("SLOTH")
            if TOC1 == TOC2:
                print("TIE")
