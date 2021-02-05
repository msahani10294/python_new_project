import re
f = open('data.txt', 'r')
content = f.read()

pattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})')
matches = pattern.findall(content)
for match in matches:
    print(match)

f.close()


