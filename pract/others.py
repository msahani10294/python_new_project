# # n = int(input("enter a no"))
# #
# # if n > 1:
# #
# #     for i in range(2, n):
# #         if n % i == 0:
# #             print("not a prime no")
# #             break
# #     else:
# #         print(n)
# # else:
# #     print(n)
#
#
#
# n = int(input("Enter a no"))
#
# for num in range(1, n+1):
#
#     if num > 1:
#
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#
#         else:
#             print(num)
#
# num

s =  {2,5,7,8}
s.remove(7)
s.add(10)
s.pop()
print(s)

s1 = s.copy()
print(s1)

m1 = {1,2, 3}
m2 = {4, 5, 6}
m3 = m1.update(m2)
print(m1)

print(m2)
print(m3)