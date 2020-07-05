class Student:
    school="Telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2 = m2
        self.m3 = m3
    def avg(self): #instance method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):  #Accessor method
        return self.m1
    def set_m1(self,value): #mutator method
        self.m1=value
    @classmethod
    def info(cls): #class method
        return cls.school
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info1(): #static method
        print("This is Student class:in abc module")


s1=Student(34,52,91)
s2=Student(85,74,30)

print(s1.avg())
print(s2.avg())

print(Student.info())
print(Student.info1())