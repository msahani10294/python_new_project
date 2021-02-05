l = [10, 20, 30, 40,40, 60,60, 70]

temp = []
m = set(l)
print(m)

temp.append(m)


n = [x for outer in temp for x in outer]
print(n)