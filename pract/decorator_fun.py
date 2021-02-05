def decorator_function(any_function):

    def wrapper_function(*args, **kwargs):
        print("wrapper function executing first")
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print("display function ran")



@decorator_function
def person(name, age):
    print("name is {} an their age is {}".format(name,age))


display()
print()
person("manoj", 24)