nums=[7,6,9,5]

print(nums[0])

for i in nums:
    print(i)

it=iter(nums)
print(it.__next__())

print(next(it))

class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values=TopTen()
for i in values:
    print(i)
print(next(values))
print(values.__next__())
print(values.__next__())
