def my_dec(any_function):
    def wrapper_function():
        print("inside wrapper function")
        return any_function()
    return wrapper_function

@my_dec
def my_fun():
    print("this is my function")

my_fun()