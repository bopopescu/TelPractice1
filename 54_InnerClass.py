class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=5

        def show(self):
            print(self.brand,self.ram,self.cpu)

s1=Student("Geetha",78)
s2=Student("Jenny",31)

print(s1.name,s1.rollno)
print(s2.name,s2.rollno)

s1.show()
s2.show()
print(s1.lap)
print(s2.lap)

