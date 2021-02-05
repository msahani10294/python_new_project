d = {n : n*n for n in range(1,10)}
print(d)


dict1 = {}

for i in range(1,10):
    dict1[i] = i

print(dict1)


dict2 = {n:(n if n%2==0 else "invalid") for n in range(1,10)}
print(dict2)

lst = [(101, "Manoj"), (102, "Mohit")]

dict4 = {k:v for k,v in lst}
print(dict4)

