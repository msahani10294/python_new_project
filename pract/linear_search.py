pos = -1


def search(lst, n):

    i = 0

    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i+=1


lst = [1, 10, 20, 40, 80, 100]
n = 80

if search(lst, n):
    print("fount at index", pos)
else:
    print("not found")