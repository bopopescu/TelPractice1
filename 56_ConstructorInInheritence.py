class A:
    def __init__(self):
        print("In A Init")
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def __init__(self):
        super().__init__()
        print("In B Init")
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C:
    def __init__(self):
        print("In C Init")

        def feature5(self):
            print("Feature 5 is working")
        def feature1(self):
            print("Feature 1 is working in C")
class D(A,C):

    def __init__(self):
        super().__init__() #MRO
        print("In D Init")
    def feature6(self):
        print("Feature 6 is working")
    def feat(self):
        super().feature2()

a1=A()
b1=B()
d1=D()
d1.feature1()
d1.feat()
