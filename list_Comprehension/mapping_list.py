l1 = ["a", "b", "c"]
l2 = [0, 1, 2]

l3 = [(a,b) for a in l1 for b in l2]
print(l3)

l4 = [i.upper() for i in l1]
print(l4)

z = list(zip(l1, l2))
print(z)