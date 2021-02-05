
sqr = [ i**2 for i in range(1, 20) ]
print(sqr)


# normal method

n = int(input("enter a no :"))
l = list(range(1, n+1))

new_sqr = []

for i in l:
    if i == 0:
        print("1")
    else:
        new_sqr.append(i**2)

print(new_sqr)
