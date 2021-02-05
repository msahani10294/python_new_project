dict1 = {'a': 30, 'b':45, 'B':5}

d = {k.lower():dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()}
print(d)

print(dict1.get('a'))