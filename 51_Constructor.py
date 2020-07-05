class Computer:
    def __init__(self):
        self.name="Geetha"
        self.age=28

    def update(self):
        self.age=30
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=Computer()
c2=Computer()
print(id(c1))
c1.name="Rashi"
c1.age=20

c1.update()
print(c1.name)
print(c1.age)
if c1.compare(c2):
    print("they are same")
else:
    print("They are different")