for i in range(int(input())):
    n= int(input())
    t = str(input())
    N = Y = I = 0
    for j in t:
        if j == "I":
            I+=1
        elif j=="N":
            N+=1
        elif j=="Y":
            Y+=1
    if I>0:
        print("INDIAN")
    elif Y and N >=1 or (Y>=1 and N==0):
        print("NOT INDIAN")
    elif (N>=1 and Y==0):
        print("NOT SURE")

