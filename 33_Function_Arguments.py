def update(x):
    x=8
    print(x)

update(10)

a=10
update(a)
print("a",a)


def update1(lst):
    print(id(lst))
    lst[1]=10
    print(id(lst))
    print("x ",lst)
lst=[12,13,14]
print(id(lst))
update1(lst)
print("lst ",lst)