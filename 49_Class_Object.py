class Computer:
    def config(self):
        print("i5,16gb,TB")


com1=Computer()

print(type(com1))
Computer.config(com1)
com1.config()