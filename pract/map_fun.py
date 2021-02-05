from functools import reduce
l = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]

# double the value

d = list(map(lambda x:x*2, l))
print(d)

# even no

even = list(filter(lambda x:x%2==0, l))
print(even)

# sum of no

sum_of_num = reduce(lambda x,y:x+y,l)
print(sum_of_num)