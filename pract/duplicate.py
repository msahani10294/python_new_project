data = [1, 2, 3, 5, 6,5,6]


def remove_duplicate(duplist):

    noduplist = []

    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist


print(remove_duplicate(data))