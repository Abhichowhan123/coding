for i in range(int(input())):
    n = input()
    m = input()
    count = 0
    for j in range(len(n)):
        if n[j]== m[j] or  m[j]== "?" or n[j]== "?":
            count+=1
    if count==len(n):
        print("Yes")
    else:
        print("No")