def check_operator():
    a, b = map(int, input().split())
    if a < b:
        print("<")
    elif a > b:
        print(">")
    elif a == b:
        print("=")

n = int(input())
for i in range(n):
    check_operator()

