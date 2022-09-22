def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(m,n):
        if m<n:
            m,n = n,m
        return func(m,n)
    return  inner

div = smart_div(div)
div(2,88)