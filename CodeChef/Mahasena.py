n = int(input())
m = input().split()
o = p = 0
for j in range(len(m)):
    if int(m[j]) % 2 == 0:
        o += 1
    else:
        p += 1
if o > p:
    print("READY OF BATTLE")
else:
    print("NOT READY")
"""

o = p = 0
n = int(input())
m = list(map(int,input().split()))
for j in range(n):
    if int(m[j]) % 2 == 0:
        o += 1
    else:
        p += 1
if o > p:
    print("READY OF BATTLE")
else:
    print("NOT READY")
"""