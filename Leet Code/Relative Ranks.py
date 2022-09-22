"""["Gold Medal","5","Bronze Medal","Silver Medal","4"]"""
score = [10]
dic = {}
w = {1:"Gold Medal",2:"Silver Medal",3:"Bronze Medal"}
for i in range(len(score)):
    dic[i] = [score[i]]
dic = sorted(dic.items(),key = lambda x:x[1],reverse=True)
q = 1
for i in range(len(dic)):
    if q<=3:
        dic[i][1].append(w[q])
    else:
        dic[i][1].append(str(q))
    q+=1
dic = sorted(dic,key = lambda x:x[0])
A= []
for r in range(len(dic)):
    A.append(dic[r][1][1])
print(A)