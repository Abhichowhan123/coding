num =a  = 16
if num == 1:
    print(True)
low, high = 1,num//2
while low < high:
    mid = (low+high)//2
    if mid*mid == num:
        print(True)
    elif mid*mid < num:
        low = mid+1
    else:
        high = mid-1
print(True)