s = "AAAAAAAAAA"
dic = {}
result = {}
i , j = 0,10

A = s[i:j]
while j!=len(s)+1:
    if A in dic:
        dic[A]+=1
        if dic[A]>=2 :
            if A not in result:
                result[A] = 1
    else:
        dic[A] =1
    i+=1
    j+=1
    A = s[i:j]
print(result.keys())