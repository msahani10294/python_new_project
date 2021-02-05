# A
# B B
# C C C
# D D D D

n = int(input("enter no of rows :"))

for i in range(n):
    print((chr(65 + i)+ ' ') * (i+1))