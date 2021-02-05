# no = ["even" if x%2==0 else "odd" for x in range(10)]
# print(no)


x = [i*i for i in range(1,10)]
print(x)

z = map(lambda x:x*x, range(1,10))
print(list(z))

l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[num2 for num1 in l1 for num2 in num1]
print (l2)