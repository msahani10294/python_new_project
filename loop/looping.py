def fib(n):
    a = 0
    b = 1

    for _ in range(n):
        print(a)
        a,b=b, a+b

fib(10)