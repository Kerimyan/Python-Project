######
######
###Python Conditions

### 1. Write a program (calculator) that will accept 2 numbers and an action(+, -, *, /, **) , the program must return the result of the given action. for example num_1 = 3 num_2 = 5 action = ' + ' result = 8
#
# list = list(input('Input 1st number, an action(+, -, *, /, **) and 2nd number: "5+2": '))
#
# x = int(list[0])
# a = list[1]
# y = int(list[2])
#
# if a == '+':
#     res = x+y
# elif a == '-':
#     res = x-y
# elif a == '*':
#     res = x*y
# elif a == '/':
#     res = x/y
# elif a == '**':
#     res = x**y
# else:
#     print('try agein: ')
#
# print(res)
#
#
# #############

### 2. Enter three integers from the keyboard. Decide which is the biggest.
#
# numbs = input('enter 3 numbers::')
# a,b,c = numbs.split()
# if a>b>c or a>c>b:
#     print("Bigest number is:", a)
# elif b>a>c or b>c>b:
#     print("Bigest number is:", b)
# else:
#     print("Bigest number is:", c)
#
##############################################


### 4. Enter a date from the keyboard (for example, 1986). Decide whether the year entered by the user is a leap year or not.
# year = int(input('Input the year: '))
# res = "this is NOT leap year:"
# for i in range(0, 2023, 4):
#     if year == i:
#         res = 'this is leap year: '
#
# print(res)
#
# #######################################


### 5. Enter two random numbers from the keyboard, one even and the other odd. Decide and display an odd number.
#
# lst_1 = input('enter numbers: ')
# lst_1 = lst_1.replace(' ', '')
#
# even = []
# odd = []
#
# for i in lst_1:
#     if int(i) % 2 == 0:
#         even += i
#     else:
#         odd += i
#
# print('even numbers is:', even)
# print('odd numbers is:', odd)
#
#######################################


### 9. Find the roots of a quadratic equation and display them on the screen, if any. If there are no roots, then display a message about it. A specific quadratic equation is determined by the coefficients a, b, and c that the user enters.
# from math import sqrt
#
# a = int(input("input 'a': "))
# b = int(input("input 'b': "))
# c = int(input("input 'c': "))
#
#
# D = b**2 - 4 * a * c
#
# if D > 0:
#     x_1 = (-b + sqrt(D)) / (2 * a)
#     x_2 = (-b - sqrt(D)) / (2 * a)
#     print('x1 is:', x_1)
#     print('x2 is:', x_2)
# else:
#     print('there is no roots!! :')
#
# #############################################################################
