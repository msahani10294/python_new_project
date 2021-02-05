# 1 2 3 4
# 1 2 3
# 1 2
# 1

n = int(input("enter no rows:"))

for i in range(n):
    for j in range(n-i):
        print(j+1, end=' ')
    print()

