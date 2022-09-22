prices =  [1]
count = 0
i = 1
while i<=len(prices):
    if prices[i]>prices[i-1]:
        count+=(prices[i]-prices[i-1])
        i+=1
    i+=1
print(count)