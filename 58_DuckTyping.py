class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")
class Laptop:
    def code(self,ide):
        ide.execute()
class MyEditor:
    def execute(self):
        print("spell check")
        print("conventio check")
        print("Compiling")
        print("Running")

lap1=Laptop()
lap1.code(MyEditor)