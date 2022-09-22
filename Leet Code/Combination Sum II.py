candidates = [1, 1, 2, 5, 6, 7, 10]
target = 8
A = []
candidates  =sorted(candidates)
def sum2(a,target,B):
	if a > len(candidates) or target<0:
		return
	if target == 0:
		A.append(B)
		return
	for i in range(a,len(candidates)):
		if i > a and candidates[i] == candidates[i-1]:
			continue
		sum2(i+1,target-candidates[i],B+[candidates[i]])
sum2(0,target,[])
print(A)
