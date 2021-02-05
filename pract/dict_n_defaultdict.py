string = "my name is manoj"
#
# d = {}
#
# for i in string:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] +=1
#
# print(d)


from collections import defaultdict

d = defaultdict(int)

for i in string:
    d[i]+=1
print(d)
