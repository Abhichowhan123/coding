s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
frequency = {}
for i in words:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
stringlen = len(words[0])
n = len(words)
check  = {}
total = stringlen*n
def rec():








# s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
# words = ["fooo","barr","wing","ding","wing"]
# i,j,n =0, len(words[0])*len(words),len(words[0])
# A = []
# while j!=(len(s)+n):
#     a = list(words)
#     st = "".join(s[i:j])
#     b= 0
#     c = n
#     w = len(st)
#     while w!=0:
#         if st[b:c] in a:
#             a.remove(st[b:c])
#             b+=n
#             c+=n
#         else:
#             break
#         w-=n
#     if  len(a)==0:
#         A.append(i)
#     i+=n
#     j+=n
# print(A)