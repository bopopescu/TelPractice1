x=int(input("How many candies you want"))
available=10
i=1
while i<=x:
    if i>available:
        print("Out of stock")
        break
    print("candy",i)
    i+=1

for k in range(1,101):
    if k%3==0 or k%5==0:
        continue
    print(k)
print("Bye")

for j in range(1,101):
    if j%2==0:
        pass
    else:
        print(j)
