def fact(n):
    prod = 1

    for i in range(1, n+1):
        prod = prod * i
    return prod


n = int(input("enter a any positive no :"))
print("factorial of {} is".format(n), fact(n))
