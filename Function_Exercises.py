### 1. Write a function to_dict () that takes a list argument and returns a dictionary in which each item in the list is
##both a key and a value. It is assumed that the elements of the list will follow the rules for specifying keys in
##dictionaries.
# dict_1 = dict()
# def to_dict(l: list):
#     for i in l:
#         dict_1[i]= i
#     return dict_1
#
# print(to_dict([1,2,3,4]))
#
#
################################



### 2. The user enters data on the number of students, their surnames, names, and scores each. The program should determine
### the average grade and display the last names and first names of students whose score is above the average.
#
# num = int(input("enter the number of students::"))
# std={}
# for i in range(num):
#     name = input("input the name of student::--->")
#     score = int(input(f"input the score of {name}::-->"))
#     std[name]=score
#
# print(std)
#
# mid = sum(std.values()) / num
#
# print(f"the average score is {mid}")
#
# print("this students have scores above the average:")
# for i in std.items():
#     if i[1] > mid:
#         print(i[0])
#
##############################


### 3. Write a program that stores data about goods, their quantity, and price. \
## When the program starts, this information is displayed on the screen. \
## Next, the user should be prompted to enter the item numbers and their new quantity.\
## Changes to data should be completed when the user enters a specially specified character (for example, 0). \
## After that, all data about the items should be displayed again.

#############################

## Matrix sorting
# x = int(input("input the 1st size"))
# z = int(input("input the 2st size"))
# import random
# matrica = [[random.randint(0, 10000) for j in range(x)] for i in range(z)]
#
#
# def calc(matrix : list, column):
#        sum = 0
#        for i in range(len(matrix)):
#               sum +=matrix[i][column]
#        return sum
#
#
# def bubble(lst: list):
#     for i in range(len(lst)):
#         for j in range(i,len(lst)):
#             if calc(lst, j) < calc(lst, i):
#                    for x in range(len(lst)):
#                      lst[x][j], lst[x][i] = lst[x][i], lst[x][j]
#     return lst
#
# for i in matrica:
#     print(i)
# print('=======================')
# for i in bubble(matrica):
#     print(i)
# #
##################################
###################################

### Calculator with functions

# x = int(input("input the 1st number:"))
# a = input("input the action:")
# y = int(input("input the 2nd number:"))
#
# def sum(x, y):
#    return x + y
# def minus(x, y):
#    return x - y
# def prode(x, y):
#    return x * y
# def bazan(x, y):
#    return x / y
#
# opr = {"+":sum(x, y),"-":minus(x, y),"*":prode(x, y),"/":bazan(x, y)}
# def option(a: str):
#     return opr[a]
#
# print(option(a))



################################
################################

### Sorting numbers by sum of digit
#
# num = input("input the numbers::")
#
# num1 = list(num.split(' '))
#
# def sum_of_dig(dig: str):
#     sum1=0
#     for i in dig:
#         i1 = int(i)
#         sum1+=i1
#     return sum1
#
# def bubble(lst: list):
#     for i in range(len(lst)):
#         for j in range(i,len(lst)):
#             if sum_of_dig(lst[j]) < sum_of_dig(lst[i]):
#                 lst[j], lst[i] = lst[i], lst[j]
#     return lst
#
# print(bubble(num1))
# #######################




