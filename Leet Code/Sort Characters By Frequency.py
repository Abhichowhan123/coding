s = "tree"
dic = {}
for i in s:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
dic = sorted(dic.items(),key= lambda x:x[1],reverse= True)
result = ""
for a,b in dic:
    result+=a*b
print(result)