def greet():
    print("hello")
    print("Good evening")

greet()

def add(x,y):
    c=x+y
    print(c)


add(4,5)

def add1(x,y):
    c=x+y
    return c


result=add1(4,5)
print(result)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(8,3)
print(result1,result2)