# ###Palindrome version 1
# import re
# s = input('input the palindrome word: ')
# s1 = re.sub(r'\W+', '', s).lower().replace('_', '')
#
# result = True
# for i in range(int(len(s1) / 2)):
#     a, *s1, b = s1
#     if a != b:
#         result = False
#         break
# print(result)

# ###Palindrome version 2
# import re
#
# s = input('input the palindrome word: ')
# p = re.sub(r'\W+', '', s).lower()
# p1 = re.sub('_', '', p)
# p2 = p1[::-1]
# print(p1)
# print(p2)
# if p1 == p2:
#     print(True)
# else:
#     print(False)



###The program has a month and a year of two dates. The user enters another date (month and year only).
###Determine if the third date ranges from the first date to the second, inclusive. Solve the problem using dict.
#
# start = {'year': 2002, 'mount': 2}
# finish = {'year': 2023, 'mount': 3}
# dat = input('input data: "year/mount"')
# year0, mount0 = int(dat.split('/')[0]), int(dat.split('/')[1])
#
#
# if year1 >= start['year'] and mount1 >= start['mount'] and year1 <= finish['year'] and mount1 <= finish['mount']:
#     print('Your data is in range of our data')
# else:
#     print('Your data is OUT of range of our data')
#
###############################

