

try:
    a = int(input("enter 1st no"))
    b = int(input("enter second no"))
    print(a/b)
    k = int(input("enter a no"))
    print(k)
except ZeroDivisionError as e:
    print("you cant divide any no by zero")


except ValueError as e:
    print("invalid input")

except Exception as e:
    print("something went wrong")


finally:
    print("bye")
