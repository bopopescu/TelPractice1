from functools import reduce

nums=[1,2,3,4,5,6,7,8,9,11,12,13,14,15]
evens=list(filter(lambda a:a%2==0,nums))
print(evens)

mapping=list(map(lambda a:a*2,evens))
print(mapping)

reduce1=reduce(lambda a,b:a+b,mapping)
print(reduce1)