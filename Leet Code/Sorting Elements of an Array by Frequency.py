for i in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    B = {}
    for i in range(len(A)):
        if A[i] in B:
            B[A[i]]+=1
        else:
            B[A[i]] = 1
    temp=sorted(B.items(),key=lambda x: x[1],reverse=True)
    for i in temp:
        for j in range(i[1]):
            print(i[0],end=" ")
    print()


# size = int(input())
# arr = list(map(int, input().split()))
# arr1 = list(set(arr))
# store = {}
# couli = []
# for ele in arr1:
#     cou = arr.count(ele)
#     if cou not in store:
#         store[cou] = list()
#         couli.append(cou)
#     store[cou].extend([ele])
# couli.sort(reverse=True)
# for ele in couli:
#     for eleme in store[ele]:
#         print((str(eleme) + " ") * ele, end="")
# print()



# arr=[5,5,4,6,4]
# n=len(arr)
# s=list(set(arr))
# dic={}
# for i in s:
#     dic[i]=arr.count(i)
# temp=sorted(dic.items(),key=lambda x: x[1],reverse=True)
# res=""
# for i in temp:
#     for j in range(i[1]):
#         print(i[0],end=" ")
# print()

# def sortbyfreq(arr, n):
#     dt = defaultdict(lambda: 0)
#     for i in range(n):
#         dt[arr[i]] += 1
#
#     arr.sort(key=lambda x: (-dt[x], x))
#
#     print(*arr)
#
# A = [5, 5, 4, 6, 4]
#
# sortbyfreq(A, len(A))