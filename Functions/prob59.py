def count_vowel():
    pass

str = "how are you"

i = 0
count = 0
vowels = 'a','e','i','o','u'

print(str[0])

while i<len(str):
    if str[i] in vowels:
        count+=1
    i+=1

print(count)


