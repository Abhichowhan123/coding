m = 3
n = 3
count = 0
def path(i,j):
    if i==(n-1) or j == (m-1):
        return 1
    return (path(i+1,j)+path(i,j+1))

print(path(i=0,j=0))
