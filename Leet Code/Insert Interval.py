intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

A = []
for i in  range(len(intervals)):
    if intervals[i][0] >newInterval[1]:
        A.append(newInterval)
        print( A+intervals[i:])
        break
    elif newInterval[0]>intervals[i][1] :
        A.append(intervals[i])
    else:
        newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
A.append(newInterval)
print(A)
