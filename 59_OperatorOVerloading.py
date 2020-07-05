a=5
b=6
print(a+b)
print(int.__add__(a,b))

x='5'
y='8'
print(str.__add__(x,y))

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def add(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    def __gt__(self, other):
        r1=self.m1+self.m2
        r2=self.m2+other.m2
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
s1=Student(45,58)
s2=Student(52,56)

#s3=s1+s2
s3=s1.add(s2)
print(s3.m1)
print(s3.m2)

print(s1.__gt__(s2))
print(s1)