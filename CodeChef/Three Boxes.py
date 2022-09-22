for i in range(int(input())):
    A,B,C,D=map(int,input().split())
    if A+B+C<=D:
        print("1")
        continue
    elif A<B==C==D or A==B<C==D or A==B==C<D:
        print("3")
        continue
    elif A+B<=C<=D or A<=B+C<=D :
        print("2")