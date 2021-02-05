sentence = input("enter any string")


def word_count(name):

    words = name.split()
    count = dict()

    for word in words:
        if word in count:
            count[word] +=1
        else:
            count[word] = 1
    return count


print(word_count(sentence))



