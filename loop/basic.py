# Prints all letters except 'e' and 's'

a = 'geeksforgeeks'

# i = 0
# while i < len(a):
#
#   if a[i]== "a" or a[i] == "s":
#       i += 1
#       continue
#
#   print(a[i])
#   i+=1


for i in range(len(a)):
    if a[i] == "a" or a[i] == "s":
        continue
    print(a[i])