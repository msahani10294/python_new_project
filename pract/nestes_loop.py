l = [[1,2,3], [4,5,6], [7,8,9]]

new_lst = []

for outer in l:
    for inner in outer:
        new_lst.append(inner)

print(new_lst)


# using list comprehension

lst = [i for outer in l for i in outer ]
print(lst)