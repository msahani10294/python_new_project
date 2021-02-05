# * * * 1
# * * 2   2
# * 3   3    3
# 4   4   4     4

n = int(input("enter no of rows: "))

for i in range(n):
    print(' '*(n-i-1)+ (str(i+1) +' ')*(i+1))