t = int(input())
for i in range (t):
    n = int(input())
    if n < 1500:
        HAR = (n*10)/100
        DA = (n*90)/100
        print(n+HAR+DA)
    elif (n>=1500):
        HAR = 500
        DA = (n * 98) / 100
        print(n + HAR + DA)