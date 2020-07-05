a=5
b=2
#b=0
try:
    print("resource open")
    print(a/b)
    k=int(input("Enter a number"))
    print(k)
except ZeroDivisionError as z:
    print("Can not divide by zero",z)
except ValueError as v:
    print("Invalid input")
except Exception as e:
    print("Hey Can not divide by zero",e)
finally:
    print("resource closed")
    print("Bye")