# l = input("enter any string:")
#
# n = reversed(l)
#
# if list(l) == list(n):
#     print("{} is  a palindrome".format(l))
#
# else:
#     print("{} is not a palindrome".format(l))


s = input("enter any string:")
try:
    if s == s[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
except ValueError:
    print("not valid input")