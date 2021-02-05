s = {1, 2, 3, 4,5 ,6}

m = {10, 20}
s.add("khalis")
print(s)

s.add(5)
print(s)


s.remove(3)

s.pop()
print(s)

s.pop()
print(s)


s.update(m)
print(s)

d = {"key1": "manoj", "key2":"24"}
d.pop("key1")
print(d)
d1 = {"key3": "manish"}
d.update(d1)
print(d)
d['key3'] = "mamoj"
print(d)