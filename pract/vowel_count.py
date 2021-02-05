mystr = str(input("Enter any sentence "))

vowel ="aeiouAEIOU"

count = {}.fromkeys(vowel, 0)

for char in mystr:
    if char in count:
        count[char]+=1

print(count)