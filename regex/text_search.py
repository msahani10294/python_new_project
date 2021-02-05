import re
f = open('data.txt', 'r')
content = f.read()
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = pattern.finditer(content)

for match in matches:
    print(match)