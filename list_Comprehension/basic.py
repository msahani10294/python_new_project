fruits = ["apple", "mango", "cherry", "kiwi"]

new_list = []

for item in fruits:
    if "a" in item:
        new_list.append(item)

print(new_list)


x = [ x for x in fruits if x if "a" in x ]
print(x)

y = [x for x in fruits if x != "apple"]
print(y)


# replace with new item

z = [x if x!= "mango" else "orange" for x in fruits]
print(z)