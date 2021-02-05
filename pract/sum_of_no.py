def sum_num(n):
    prod = 0

    for i in range(0, n+1):
        if i % 2 == 0:
            prod = prod + i
    return prod


print(sum_num(10))