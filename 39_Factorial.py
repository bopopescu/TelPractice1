n=5

def fact(n):
    f = 1
    while n>0:
        f=f*n
        n-=1
    print(f)



fact(n)


def fact1(n):
    f1 = 1
    for i in range(1,n+1):
        f1=f1*i
    print(f1)

fact1(6)