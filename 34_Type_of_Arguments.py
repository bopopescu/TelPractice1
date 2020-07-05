def add(a,b):
    c=a+b
    print(c)

add(9,3)

def person(name,age=18): #default value 18
    print(name,age)

person("geetha",30)
person(age=28,name="seetha")
person("Neetha")

def sum(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i
    print(c)

sum(4,5,8,9)

