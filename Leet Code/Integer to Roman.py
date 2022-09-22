num =9

# Output: "MCMXCIV"
A  = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
dic = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
S = ""
i = 0
while num>0:
    div  = num//A[i]
    num = num%A[i]
    while div:
        S = S+dic[A[i]]
        div  =div-1
    i+=1
print(S)