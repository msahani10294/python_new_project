students = {}

student1 = {'name':"manoj", "subject":{"maths" :20, 'science':30, 'physics':40}}
student2 = {'name':"khalis", "subject":["maths", 'science', 'physics'], 'marks': [90, 30, 80]}
student3 = {'name':"Asif", "subject":["maths", 'science', 'physics'], 'marks': [70, 50, 55]}


students['student1'] = student1
students['student2'] = student2
students['student2'] = student3
print(students)


a = (students['student1']['subject'])
print(a)
# b = students(['student1']['marks'])
# print(b)


# print(dict(zip(a,b)))