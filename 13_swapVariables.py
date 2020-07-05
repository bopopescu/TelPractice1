a=5
b=6
temp=a
a=b
# way 1
b=temp
print(a)
print(b)


# way 2
a=3
b=4
a=a+b
b=a-b
a=a-b
print(a)
print(b)

# way 3
#1 bit will be wasted 11+41=52
a=11
b=41
a=a^b
b=a^b
a=a^b
print(a)
print(b)

# way 4
#stack rotation
a=8
b=9
a,b=b,a
print(a)
print(b)

