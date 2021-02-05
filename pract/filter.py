# n = int(input("enter a no :"))
# l = list(range(1, n+1))
#
# temp = []
#
# for i in l:
#     temp.append(i)
#
# print(temp)
# even_no = list(filter(lambda x:x%2==0, temp))
# print(even_no)

def startwith(x):
    if len(x) > 0:
        return x[0] == "m"
    else:
        return ("letter m  is not present")

name = ["manoj", "manish", "john"]

name_lst = list(filter(startwith, name))
print(name_lst)