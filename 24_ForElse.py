nums=[12,14,15,16,71,25,94,30]
#nums=[12,14,16,71,94]
for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("Not found")
