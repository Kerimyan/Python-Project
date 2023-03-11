### 1. Count the even and odd digits of the entered natural number. For example, if the number 34560 is entered, then it has 3 even digits (4, 6, and 0) and 2 odd digits (3 and 5).
#
# num = input('please enter any number: ')
# even = []
# odd =[]
# for i in num:
#     if int(i) % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# else:
#     print(f'even numbers is : {even}')
#     print(f'odd numbers is : {odd}')
#
# ###############################

### 2. Find the sum and product of the digits of the entered natural number. For example, if the number 325 is entered, then the sum of its digits is 10 (3+2+5), and the product is 30 (325).
#
# num = input('Please enter the number:: ')
#
# while not (num != 0 and len(num) > 1):
#     num = input("Try again: Number must be great then 0::")
#
# sum = 0
# prod = 1
#
# for i in num:
#     sum += int(i)
#     prod *= int(i)
# else:
#     print(f"SUM: {sum}")
#     print(f"Prod: {prod}")
#
# ################################################

### 3. Print a series of natural numbers on the screen from minimum to maximum with a step. For example, if the minimum is 10, the maximum is 35, and the step is 5, then the output should be: 10 15 20 25 30 35. The user specifies the minimum, maximum, and step (read from the keyboard).
#
# while True:
#     lst = input("Please enter the start number, finish number and step::'1:10:3'")
#     if ':' in lst:
#         break
#
# strt, fin, step = int(lst.split(":")[0]), int(lst.split(":")[1]), int(lst.split(":")[2])
#
# for i in range(strt, fin, step):
#     print(i)
#
# #########################


### 5. Display as many elements of the Fibonacci series as the user has specified. For example, if the input received the number 7, then the output should contain the first six numbers of the Fibonacci series: 1 1 2 3 5 8 13.
#
# n = int(input("::How many fibonacci numbers do you want to print::"))
#
# lst = [1,1]
#
# for i in range(n-2):
#     s = i+1
#     num_3 = lst[i] + lst[s]
#     lst.append(num_3)
# else:
#     print(lst)
#
# ########################################
#
### 7. The program generates a random integer from 0 to 100. The user must guess it in no more than 10 attempts. \
#    After each unsuccessful attempt, more or less the number entered by the user should be reported than what is guessed. \
#    If in 10 attempts the number is not guessed, then output the hidden number.
# import random
# x = random.randint(1, 100)
#
# n_try = 10
# num = int(input(f"Try to guess the number: (You have {n_try} try:)"))
#
# while num != x:
#         n_try -= 1
#         if n_try == 0:
#             print("you have failed!!")
#             print("!!Game over!!")
#             break
#         if n_try == 1:
#             print ("Last chanցe!!!!")
#         else:
#             print (f"NOT corect; Try again (You have only {n_try} try:)")
#         if num > x:
#             num = int(input("X number is smaller::"))
#         else:
#             num = int(input("X number is biger::"))
# else:
#     print("!!!Congratulations. You have guessed the number:!!!!")
#     print("Game over!")
#
# ###################################


### 10. Write a program that will add, subtract, multiply, or divide two numbers. The numbers and signs of the operation are \
## entered by the user. After completing the calculation, the program should not terminate but should request new data for calculations. \
## The end of the program must be carried out by entering the character '0' as an operation character. \
## If the user enters an invalid character (not ‘0’, ‘+’, ‘-’, ‘*’, ‘/’), then the program should inform him about the error and ask again for the character of the operation. \
## Also, inform the user about the impossibility of dividing by zero if he entered 0 as a divisor.
#
# print('Input 1st number, an action(+, -, *, /, **) and 2nd number: "5+2": (For exit input 0 0 0) ')
# while True:
#     try:
#         x, a, y = input('------>').split()
#     except ValueError:
#         print('try again!')
#         continue
#     if x == '0' and y == '0' and a == '0':
#         print('END')
#         break
#     try:
#         x = int(x)
#         y = int(y)
#     except ValueError:
#         print('Try again!')
#         continue
#     if a  == '+' or a == '-' or a == '*' or a == '**' or a == '/':
#         if a == '+':
#             res = x+y
#         elif a == '-':
#             res = x-y
#         elif a == '*':
#             res = x*y
#         elif a == '/':
#             res = x/y
#         elif a == '**':
#             res = x**y
#     else:
#         print("Incorrect option")
#         continue#
# print('Input 1st number, an action(+, -, *, /, **) and 2nd number: "5+2": (For exit input 0 0 0) ')
# while True:
#     try:
#         x, a, y = input('------>').split()
#     except ValueError:
#         print('try again!')
#         continue
#     if x == '0' and y == '0' and a == '0':
#         print('END')
#         break
#     try:
#         x = int(x)
#         y = int(y)
#     except ValueError:
#         print('Try again!')
#         continue
#     if a  == '+' or a == '-' or a == '*' or a == '**' or a == '/':
#         if a == '+':
#             res = x+y
#         elif a == '-':
#             res = x-y
#         elif a == '*':
#             res = x*y
#         elif a == '/':
#             res = x/y
#         elif a == '**':
#             res = x**y
#     else:
#         print("Incorrect option")
#         continue
#     print(f"{x} {a} {y} = {res}")
#
# ##################################

#     print(f"{x} {a} {y} = {res}")
#
# ##################################
