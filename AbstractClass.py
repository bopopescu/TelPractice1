from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        #print("Running")
        pass
class Laptop(Computer):
    def process(self):
        print("Running")

class Programmer:
    def work(self,com):
        print("Solving bugs")
        com.process()
class Whiteboard(Computer):
    def write(self):
        print("its writing")

#com=Computer()
#com.process()
com1=Laptop()
com1.process()
prog1=Programmer()
prog1.work(com1)
com2=Whiteboard()
prog1.work(com2)
