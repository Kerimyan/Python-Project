import re
s = input('input the palindrome word: ')
s1 = re.sub(r'\W+', '', s).lower().replace('_', '')

result = True
for i in range(int(len(s1) / 2)):
    a, *s1, b = s1
    if a != b:
        result = False
        break
print(result)