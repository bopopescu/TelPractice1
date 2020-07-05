a=10
print(id(a))
def something():
    #global a
    a=15
    print("local",a) #local
    x=globals()['a']
    print(id(x))
    print("global in func", a)  # global
    globals()['a']=18

something()
print("global",a) #global