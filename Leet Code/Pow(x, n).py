# def power(x,n):
#     if n ==0:
#         return 1
#     k = power(x,n//2)
#     if (n%2 == 0):
#         return k*k
#     else:
#         return k*k*x
# n = 10
# x = 2
# print(power(x,n))
class Solution:

    def myPow(self, x: float, n: int) -> float:

        def power(x, n):
            print(n)
            if n == 0:
                return 1
            k = power(x, n // 2)
            if (n % 2 == 0):
                return k * k
            else:
                return k * k * x
        if (n >= 0):
            return (power(x, n))
        else:
            return 1 / (power(x, -1 * n))

# def power(x, n):
#     print(n)
#     if n == 0:
#         return 1
#     k = power(x, n // 2)
#     if (n % 2 == 0):
#         return k * k
#     else:
#         return k * k * x
#     # if (n >= 0):
#     #     return (power(x, n))
#     # else:
#     #     return 1 / (power(x, -1 * n))
#
# x = 2
# n=10
# if (n >= 0):
#     print (power(x, n))
# else:
#     return 1 / (power(x, -1 * n))