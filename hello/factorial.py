def factorial(a):

    b=1
    for i in range (1,a+1):
        b=b*i
        print(b)


n=int(input("enter the no for factorial"))
factorial(n)