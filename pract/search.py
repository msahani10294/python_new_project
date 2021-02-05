def search(lst, n):
    for i, val in enumerate(lst):
        if val == n:
            return i
    return  "not found"


lst = [1,2,3,4,5,6]

print(search(lst, 5))