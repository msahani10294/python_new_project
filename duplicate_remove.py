l = [1, 2, 3, 4, 5, 6, 1,2, 3, 5,6,5,6]

def duplicate(data):

    temp = []

    for i in range(data):
        if i not in data:
            temp.append(i)
            print(temp)
duplicate(l)