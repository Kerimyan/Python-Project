# # 1 Integers Data Types
# # print(type(100))
# # print(sys.getsizeof(0))
# # print(sys.getsizeof(1))
# # print(sys.getsizeof(28*1000))
# # print(2**1000)
# # print(2**10000)
# # def calc(a):
# #     for i in range(10000000):
# #         a * 2
# # start=time.perf_counter()
# # calc(2**100)
# # end = time.perf_counter()
# # print(end-start)
# # start=time.perf_counter()
# # calc(2**10000)
# # end = time.perf_counter()
#
# # 2 Integers Operations
# # print(13%4)
# # #13%4
# # print(-13%4)
# # #(-13)%4=3
# # print(13%-4)
# # #13%(-4)=-3
# # print(-13%-4)
# # #(-13)%(-4)
# # print(type(1+1))
# # print(type(2*3))
# # print(type(3**6))
# # print(type(2/3))
# # print(math.floor(3.999999))
# # print(math.floor(-3.999999))
# # print(math.floor(-3.0000001))
# # print(math.floor(-3.0000000000000001))
# # a =33
# # b =16
# # print(a/b,a//b,math.floor(a/b))
# # a=-33
# # b =16
# # print(a/b,a//b,math.floor(a/b))
# # a = 7
# # b = -4
# # print(a/b,a//b,math.floor(a/b),math.trunc(a/b))
# # a = b * (a//b) + (a%b)
# # a = 13
# # b = 4
# # print('{0}/{1} = {2}'.format(a, b, a/b))
# # print('{0}//{1}={2}'.format(a, b, a//b))
# # print('{0}%{1}={2}'.format(a, b, a%b))
# # print(a == b * (a//b) + (a%b))
# #
# # a= -13
# # b = 4
# # print('{0}/{1} = {2}'.format(a, b, a/b))
# # print('{0}//{1}={2}'.format(a, b, a//b))
# # print('{0}%{1}={2}'.format(a, b, a%b))
# # print(a == b * (a//b) + (a%b))
# #
# # a= 13
# # b = -4
# # print('{0}/{1} = {2}'.format(a, b, a/b))
# # print('{0}//{1}={2}'.format(a, b, a//b))
# # print('{0}%{1}={2}'.format(a, b, a%b))
# # print(a == b * (a//b) + (a%b))
# #
# # a= -13
# # b = -4
# # print('{0}/{1} = {2}'.format(a, b, a/b))
# # print('{0}//{1}={2}'.format(a, b, a//b))
# # print('{0}%{1}={2}'.format(a, b, a%b))
# # print(a == b * (a//b) + (a%b))
#
# # 3. Integers Constructors and Bases - Lecture
# # a = int(10)
# # print(a)
# # a = int(10.9)
# # print(a)
# # a=int(-10.9)
# # print(a)
# # a = int(True)
# # print(a)
# # a = int("10")
# # print(a)
# # print(bin(10))
# # print(oct(10))
# # print(hex(10))
# # print(int('0xA',16))
# # a=0b1101
# # print(a)
# # a = 0o123
# # print(a)
# # n = 232
# # b = 5
#
# # 3 Integers Constructors and Bases - Lecture
# # print(int('1010',base=2))
# # print(int("A12F", base=16))
# # print(int("a12f",base=16))
# # print(int('A',base=11))
# # print(int("b",12))
# # # klini bayc 11@ che
# # print(bin(10))
# # print(oct(10))
# # print(hex(10))
# # print(int('0xA',16))
# # a=0b1010
# # print(a)
# # b=0o123
# # print(b)
# # c=0x123Fa
# # print(c)
#
# # 4. Integers Constructors and Bases - Coding
# # a=int()
# # print(type(a))
# # print(type(10.9))
# # print(type(True))
# # import fractions
# # a = fractions.Fraction(22,7)
# # print(float(a))
# # print(int(a))
# # print(int("12345"))
# # print(int("FF", 16))
# # print(int("ff", 16))
# # print(int('b',12))
# # # bayc 11@ chi lini
# # print(bin(5))
# # print(oct(45))
# # print(hex(255))
# # a = int('101',2)
# # print(a)
# # b=0b101
# # print(b)
# # def from_base10(n, b):
# #     if n < 0:
# #         raise ValueError('number n must be >=0')
# #     if n == 0:
# #         return [0]
# #     if n < 2:
# #         raise ValueError('Base b must be >=2')
# #     digits = []
# #     while n > 0:
# #         n, m = divmod(n, b)
# #         if m == 10:
# #             m = "A"
# #         if m == 11:
# #             m = "B"
# import abc
# import random
# import math


# #, [27.02.23 23:32]
# #         if m == 12:
# #             m = "C"
# #         if m == 13:
# #             m = "D"
# #         if m == 14:
# #             m = "E"
# #         if m == 15:
# #             m = "F"
# #         # n, m = n // b, n % b
# #         digits.insert(0, m)
# #     return digits
# #
# #
# # #
# # #
# # # print(from_base10(4062, 16))
# # #
# # #
# # def encode(digits, digit_map):
# #     if max(digits) >= len(digit_map):
# #         raise ValueError("Digit_map is not long enough to encode the digits")
# #     return ''.join([digit_map[d] for d in digits])
# #
# #
# # #
# # #
# # # print(encode([15, 15], '0123456789ABCDEF'))
# # def rebase_from10(number, base):
# #     digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# #     if base < 2 or base > 36:
# #         raise ValueError('Invalid base: 2 <= base <=36')
# #     # sign = -1 if number < 0 else 1
# #     if number < 0:
# #         sign = -1
# #     else:
# #         sign = 1
# #     # number =number*sign
# #     number *= sign
# #     digits = from_base10(number, base)
# #     encoding = encode(digits, digit_map)
# #     if sign == -1:
# #         encoding = '-' + encoding
# #     return encoding
# #
# #
# # e = rebase_from10(3451, 16)
# # print(e)
# # print(int(e, base=16))
# # e = rebase_from10(314,2)
# # print(e)
# # print(int(e,base=2))
#
# # 1 Rational Numbers - Lecture
# # x = Fraction(math.pi)
# # print(x)
# # x = Fraction(.75)
# # x = Fraction(1.375)
# # x = Fraction(math.sqrt(2))
# # x = Fraction(True)
# # # print(type(x))
# # print(.125)
# # print(x)
# # x = format(0.3, '.5f')
# # x = format(0.3, '.25f')
# # print(x)
# # x=Fraction(0.5)
# # x.limit_denominator(100)
# # # x=Fraction(22,7)
# # print(x)
#
# # 2. Rationals Numbers - Coding
# # help(Fraction)
# # print(Fraction(denominator=1, numerator=2))
# # print(Fraction(numerator=2, denominator=3))
# # print(Fraction(0.125))
# # print(Fraction('22/7'))
# # x = Fraction(2,3)
# # y = Fraction(3,4)
# # z = x +y
# # print(z)
# # z1 = x * y
# # print(z1)
# # z2 = x * y
# # print(z2)
# # print(Fraction(8,16))
# # print(Fraction(-1,4))
# # x = Fraction(1,-4)
# # print(x)
# # print(x.numerator,x.denominator)
# # x = Fraction(math.pi)
# # print(float(x))
# # y = Fraction(math.sqrt(2))
# # print(y)
# # print(float(y))
# # a = .125
# # print(a)
# # b= 0.3
# # print(b)
# # print(Fraction(a))
# # print(Fraction(b))
# # print(format(b,'0.5f'))
# # print(format(b,'0.15f'))
# # print(format(b,'0.25f'))
# # print(Fraction(b))
# # x= Fraction(.3)
# # print(x.limit_denominator(10))
# # x = Fraction(math.pi)
# # print(x)
# # print(float(x))
# # print(x.limit_denominator(10))
# # print(22/7)
# # print(x.limit_denominator(100000))
#
# # 3. Floats Internal Representations - Lecture
# # 4. Floats Internal Representations - Coding
# # help(float)
# # print(float(10))
# # print(float(10.4))
# # print(float('12.5'))
# # print(float('22/7'))
# # error
# # a = Fraction('22/7')
# # print(float(a))
# # print(.1)
# # print(format(.1, '.15f'))
# # print(format(.1, '.25f'))
# # print(0.125)
# # print(1/8)
# # print(format(.125, '.25f'))
# # a= .1+.1+.1
# # b=.3
# # print(a==b)
# # print(format(a,'.25f'),format(b,'.25f'))
#
# # 5 Floats Equality Testing - Lecture
# # x = 0.1 + 0.1 + 0.1
# # y =0.3
# # print(format(x,'.25f'),format(y,'.25f'))
# # print(round(0.1 + 0.1 + 0.1, 5) == round(0.3, 5))
# # x = 0.1 + 0.1 + 0.1
# # y = 0.3
# # print(round(x, 5), round(y, 5), format(x, '.1f'), format(y))
# # print(round(x,5),round(y,5))
# # def is_equal(x,y,eps):
# #     format(x,'.1f')
# #     format(y,'.1f')
# #     z = math.fabs(x-y) <= eps
# #     return z
# # print(is_equal(0.1,0.1,0.2))
# # x = 0.1 + 0.1 + 0.1
# # y = 0.3
# # print(format(x, '.20f'))
# # print(format(y, '.20f'))
# # print(abs(x))
# # abs_tol = 1000e-3
# # print(math.fabs(x - y) < abs_tol)
# # print(abs_tol)
# # print(math.isclose(1.233,1.2330000))
#
# # 6 Floats Equality Testing - Coding
# # x = 0.1
# # print(format(x,'.25f'))
# # print(x)
# # x = .125
# # print(format(x, '.25f'))
# # x = .125 + .125 + .125
# # y = .375
# # print(x==y)
# # x = 0.1 + 0.1 + 0.1
# # y =0.3

# #, [27.02.23 23:32]
# # # print(x==y)
# # print(format(x,'.25f'))
# # print(format(y,'.25f'))
# # print(round(x,3) == round(y,3))
# # x = 10000.01
# # y = 10000.02
# # print(round(x,1)==round(y,1))
# # # print(y/x)
# # x = 0.01
# # y = 0.02
# # print(round(x,1) == round(y,1))
# # print(y/x)
# # delta is 0.01
# # print(help(isclose))
# # x = 0.1 + 0.1 + 0.1
# # y = 0.3
# # print(isclose(x, y))
# # print(x == y)
# # x = 123456789.01
# # y = 123456789.02
# # print(isclose(x, y, rel_tol=0.01))
# # x = 0.01
# # y = 0.02
# # print(isclose(x, y, rel_tol=0.01,))
# # x = 0.0000001
# # y = 0.0000002
# # print(isclose(x,y,rel_tol=0.01))
# # print(isclose(x,y,abs_tol=0.01))
# # x = 0.0000001
# # y = 0.0000002
# # a = 123456789.01
# # b = 123456789.02
# # print(isclose(x,y,abs_tol=0.0001,rel_tol=0.01))
# # print(isclose(a,b,abs_tol=0.0001,rel_tol=0.01))
#
# # 7 Floats Coercing to Integers - Lecture.
# # print(math.ceil(11.1))
# # print(math.trunc(12.4))
# # print(math.floor(11.4))
# # print(round(11.4))
# # a = 5
# # b = 2
# # print(a // b == math.floor(a / b))
#
# # 8. Floats Coercing to Integers - Coding.
# # help(trunc)
# # print(trunc(10.3), trunc(10.5), trunc(10.9))
# # help(int)
# # print(int(10, 4), int(10, 5), int(10, 9))
# # help(floor)
# # print(floor(10.4), floor(10.5), floor(10.9))
# # print(trunc(-10.4), trunc(-10.5), trunc(-10.9))
# # print(floor(-10.4), floor(-10.5), floor(-10.9))
# # print(ceil(-10.4),ceil(-10.5),ceil(-10.9))
# # print(ceil(10.4), ceil(10.5), ceil(10.9))
#
# # 9. Floats Rounding - Lecture
# # 10. Floats Rounding - Coding
# # help(round)
# # a = round(1, 9)
# # print(a, type(a))
# # a = round(1.9, 0)
# # print(a, type(a))
# #### n > 0
# # print(round(1.8888,3),round(1.8888,2),round(1.8888,1),round(1.8888,0))
# #### n < 0
# # print(round(888.88,1),round(888.88,0),round(888.88,-1),round(888.88,-2),round(888.88,-3),round(888.88,4))
# # print(round(9800,-4))
# # print(round(800,-4))
# # print(round(1.25,1))
# # print(round(1.35,1))
# # print(round(-1.25, 1), round(-1.35, 1))
# # def _round(x):
# #     return int(x + 0.5 * copysign(1, x))
# #
# #
# # print(round(1.5), _round(1.5))
# # print(round(-1.5), _round(-1.5))
# # print(round(2.5), _round(2.5))
# # print(round(-2.5), _round(-2.5))
#
# # 1 Boolean
# # print(int(True))
# # print(id(True) == id(1))
# # print(True > False)
# # print((1 == 2) == False)
# # print((1 == 2) == 0)
# # print(True + True + True)
# # print(-True)
# # print(100 * True)
# # print(bool(0))
# # print(bool(1))
# # print(bool(100))
# # print(bool(-1))
# # help(bool)
# # print(issubclass(bool, int))
# # print(type(True), id(True), int(True))
# # print(type(False), id(False), int(False))
# # print(3 < 4)
# # print(type(3 < 4))
# # print(id(3 < 4))
# # print(id(3 > 4))
# # print((3 < 4) == True)
# # print((3 < 4) is True)
# # print((3 > 4) == False)
# # print((3 > 4) is False)
# # print(1 == 2 and False)
# # print(int(True), int(False))
# # print(100 * False)
# # print(True > False)
# # print(True + True + True) %2
# # print(True and False)
# # print(True or False)
# # print(True is False)
# # print(bool(0))
# # print(bool(1))
# # print(bool(False),bool(True),bool(100))
#
# # 2. Booleans Truth Values - Lecture.
# # ete None,False 0 datark list tuple string bool len
# # print(bool(x))
# # print(x.bool())
# # or len bool
# # def bool(self):
# #     return self !=0
# # print(bool(1))
# # print(bool([1,2,3]))
# # print(bool([]))
# # print(bool(None))
# # print('abc')
# # print('')
# # print(bool(0))
# # print(Decimal('0.0'))
# # print(bool(-1))
# # print(bool(1+2j))
# # print(bool('0.1'))
#
# # 3. Booleans Truth Values - Coding
# # print(bool(0), (0).bool())
# # print(bool(1), (1).bool())
# # help(list)
# # print(bool(0))
# # a = []
# # print(bool(a))
# # print(a.len())
# # print(bool(0.0), bool(0 + 0j))
# # print(Fraction(0, 1)), bool(Decimal('0.0'))
# # print(bool(10.5), bool(1j), bool(Fraction(1, 2)), bool(Decimal('10.5')))
# # a =  []
# # b = ''
# # c = ()
# # print(bool(a),bool(b),bool(c))
# #
# # a =  [1,2]
# # b = 'Sa'
# # c = (1,2)
# # print(bool(a),bool(b),bool(c))
# # a = {}
# # b= {1,2}

# #, [27.02.23 23:32]
# # c = set()
# # print(a,b,c)
# # print(bool(a),bool(b),bool(c))
# # print(bool(None))
# # a = [1, 2, 3]
# # if a is not None and len(a) > 0:
# #     print(a[0], a[2])
# # else:
# #     print('Nothing to see here...')
# # a = []
# # if bool(a):
# #     print(a[0])
# # else:
# #     print('Nothing to see here...')
# #
# # a = None
# # if bool(a):
# #     print(a[0])
# # else:
# #     print('Nothing to see here...')
# #
# # a = [1, 2]
# # a = []
# # a = None
# # #### ERROR
# # if a is not None and len(a) > 0:
# #     # if len(a) > 0 and a is not None:
# #     print(a[0])
# # else:
# #     print('Nothing to see here...')
#
# # 4. Booleans Precedence and Short-Circuiting - Lecture
# # X Y   not X  X and Y  X or Y
# # 0 0     1       0       0
# # 0 1     1       0       1
# # 1 0     0       0       1
# # 1 1     0       1       1
# x, y, c = 1, 2, 3
# # print(not (not x) == x)
# # print(x or y == b or a)
# # print(x or y == b and a)
# # print(x and (y or c) == (x and y) or (x and c))
# # print(x or (y or c) == (x and y) or (x and c))
# # print(x or y or c)
# # print(not(x or y) == (not x) and (not y))
# # print(not(x and y) == (not x) or (not y))
# # print(not (x < y) == x >= y)
# # print(not (x > y) == x <= y)
# # print(True or True and False)
# # print((True or True) and False)
# # print(True or (True and False))
# # print(x < y or x > c and not x or y)
# # print((x < y) or ((x > c) and (not x)) or y)
#
# # if symbol in watch_list:
# #     if price(symbol) > treshold:
# # do something
#
# # if symbol in watch_list and price(symbol) > treshold:
# # do something
#
# # 5. Booleans Precedence and Short-Circuiting - Coding
# # not --> and --> or
# # print(True or (True and False))
# # print((True or True) and False)
# # a = 10
# # b = 2
# # if a / b > 2:
# #     print('a is at least twice b')
#
# # a = 10
# # b =
# # if a / b > 2:
# #     print('a is at least twice b')
#
# # if b > 0 and a / b > 2:
# #     print('a is at least twice b')
#
# # a = 10
# # b = 2
# # if b > 0:
# #     if a/b > 2:
# #         print('a is at least twice b')
#
# # help(string)
# # a = 'c'
# # print(a in string.ascii_uppercase)
# # print(string.ascii_uppercase)
# # print(string.digits)
# # print(string.ascii_letters)
# # name = 'Bob'
# # if name[0] in string.digits:
# #     print("Name cannot start with a digit.")
# # elif name[1] in string.ascii_uppercase:
# #     print("Name is started a Upper_case: ")
# # else:
# #     print("hi!")
#
#
# # name = ''
# # if len(name) and name[0] in string.digits:
# #     print("Name cannot start with a digit.")
# # else:
# #     print("che")
#
# # name = 'abc'
# # print(bool(name))
#
# # name = ''
# # print(bool(name))
#
# # name = None
# # if name is not None and len(name) > 0 and name[0] in string.digits:
# #     print("Name cannot start with a digit.")
#
# # name = None
# # if name and name[0] in string.digits:
# #     print("Name cannot start with a digit.")
#
### 6. Booleans Boolean Operators - Lecture
# # 7. Booleans Boolean Operators - Coding.
# # print('a' or [1, 2])
# # print('' or [1, 2])
# # print(1 or 1 / 0)
# # print(0 or 1 / 0)
# # s1 = None
# # s2 = ''
# # s3 = 'abc'
# # s1 = s1 or 'n/a'
# # s2 = s2 or 'n/a'
# # s3 = s3 or 'n/a'
# # print(s1, s2, s3)
# # print([] or [0])
# # print(None or [0])
# # print(None and 100)
# # print([] and [0])
# # a = 2
# # b = 4
# # print(a/b)
#
# # a = 2
# # b = 0
# # print(a/b)
# # if b == 0:
# #     print(0)
# # else:
# #     print(b and a/b)
#
# # s1 = None
# # s2 = ''
# # s3 = 'abc'
# # print((s1 and s1[0]) or 'n/a')
# # print((s2 and s2[0]) or 'n/a')
# # print((s3 and s3[0]) or 'n/a')
#
# # help(bool)
# # print(not True)
# # print(bool(''))
# # print(not(bool('')))
# # print(notbool(None))
#
# # 1. Introduction
# # 2. Multi Line Statements and Strings in Python
# # a = [1, #item1
# #      2, #item2
# #      3  #item3
# #      ]
# # print(a)
#
# '''This is
# a multi-line string'''
#
# """This is
# a multi-line string"""
#
#
# # a = [1, 2, 3]
# # a = [1, 2,
# #      3, 4, 5]
# # print(a)
# # a = (1
# #      , 2
# #      , 3)
# # print(a)
# # a = {'key1': 1

# #, [27.02.23 23:32]
# #     , 'key2': 2}
# # print(a)
#
#
# # def my_func(a,  # 1
# #             b,  # 2
# #             c):
# #     print(a, b, c)
#
#
# # a = 10
# # b = 20
# # c = 30
# # if a > 5 \
# #     and 5 > 10 \
# #         and c > 20:
# #     print('yes')
#
# # a = '''This is a string'''
# # print(a)
# # a = '''This
# #  is a string'''
# # print(a)
# #
# # def my_func():
# #     a = '''a multi-line string
# #     that is indented in the second line'''
# #     return a
# # print(my_func())
####
### 2. Sequence Types - Lecture
# # x = [1,2]
# # a = x + x
# # print(a)
# # x1 = 'python'
# # a = x1 + x1
# # print(a)
# # x = [[0,0]]
# # z = x+x
# # print(z[1])
# # print(z[0] is z[1])
# # x = [[0,0]]
# # a = x + x
# # a[0][0] = 100
# # print(a)
# #
# # a = [1,2] * 2
# # a = 'python' * 2
# # a = [ [0,0] ] * 2
# # print(a)
# # a = ['python'] *2
# # print(a)
#
### 3. Sequence Types - Coding.
# # i = [1,2,3]
# # t = (1,2,3)
# # s = 'python'
# # print(i[0],t[1],s[3])
# # for c in s:
# #     print(c)
# # s = [10,20,30]
# # for e in s:
# #     print(e)
#
# # s = {'x', 10, 'a', 'A'}
# # for e in s:
# #     print(e)
#
# # l = [1,2,3]
# # t = (1,2,3)
# # print(l[0])
# # print(l)
# # print(t[0])
#
# # t = ([1,2],3,4)
# # t[0][0] = 100
# # print(t[0])
# # print('a' in ['a', 'b' ,100])
# # print(100 in range(200))
#
# # 4. Mutable Sequence Types - Lecture.
# # names = ['Eric', 'John']
# # name = names + ['Michael']
# # names.append('Michael')
# # print(names)
# # s[i] = x
# # s[i:j] = s2
# # del s[i]
# # 5. Mutable Sequence Types - Coding.
# # l = [1,2,3,4,5]
# # print(id(l))
# # print(l[0])
# # l[0] = 'a'
# # print(l)
# # print(id(l))
# # l.clear()
# # print(l)
# # print(id(l))
# # l = [1,2,3,4,5]
# # print(id(l),l)
# # l = []
# # print(l)
# # print(id(l))
# # suits = ['Spades', 'Hearts', 'Diamons', 'Clubs']
# # alias = suits
# # print(id(alias),id(suits))
# # alias.clear()
# # print(alias)
# # print(suits)
# # suits = ['Spades', 'Hearts', 'Diamons', 'Clubs']
# # def something(l):
# # l.append('None')
# # l.clear()
# # print(something(suits))
# # print(suits)
# # l = [1,2,3,4,5]
# # print(id(l))
# # print(l[0:2])
# # l[2:4] = ('a','b','c','d')
# # print(l)
# # print(id(l))
# # l = [1,2,3]
# # l += [4]
# # print(l)
# # print(id(l))
# # l = [1,2,3]
# # a = l.append(4)
# # print(type(a))
# # print(a)
# # l.append([1,2,3,4])
# # print(l)
# # l = [1,2,3]
# # print(id(l))
# # l.extend([4])
# # l.extend(['a','b','c'])
# # print(l)
# # l.extend({'X','a','A',100_000})
# # print(l)
# # l = [1,2,3,4]
# # print(id(l))
# # result = l.pop(2)
# # print(l)
# # del l[1]
# # print(l)
# # print(id(l))
# # l = [1,2,3,4]
# # print(id(l))
# # l.insert(1,'a')
# # print(l)
# # l = [1, 2, 3]
# # l2 = l[::-1]
# # print(l2)
# # l.reverse()
# # print(l)
# # l = [1, 2, 3, 4]
# # print(id(l), id(l2))
# # l3 = l.copy()
# # print(l3)
# # l = [['a', 'b'], 'c', 'd']
# # print(id(l), id(l[0]), id(l[1]))
# # l2 = l.copy()
# # print(id(l2))
# # print(l2)
# # print(id(l2[0]), id(l2[1]))
# # l[0].append('x')
# # print(l)
# # print(l[::-1])
# # print(l)
#
# # 6. Lists vs Tuples.
# # print((1, 2, 3))
# # print([1, 2, 3])
# # print(dis(compile('(1,2,3,"a")', 'string', 'eval')))
# # print(dis(compile('[1,2,3,"a"]', 'string', 'eval')))
# # print(dis(compile('(1,2,3,[10,20])', 'string', 'eval')))
# # print(timeit("(1,2,3,4,5,6,7,8,9)", number=10_000_000))
# # def fn1():
# #     pass
#
#
# # print(dis(compile('fn1,10,20','1','eval')))
# # print(dis(compile('(1,2,3,[10,20])','string','eval')))
# # print(dis(compile('1,2,3,[10,20]','string','eval')))
# # print(timeit("([1,2],10,20)", number=1_000_000))
# # print(timeit("[[1,2],10,20]", number=1_000_000))
# # l1 = [1,2,3,4,5,6,7,8,9]
# # t1 = (1,2,3,4,5,6,7,8,9)
# # print(id(l1),id(t1))
# # l2 = list(l1)
# # print(id(l1),id(l2))
# # t2 = tuple(t1)
# # print(id(t1),id(t2))
#
# # print(timeit('tuple((1,2,3,4,5))', number=5_000_000))
# # print(timeit('list((1,2,3,4,5))', number=5_000_000))
# # t = tuple()
# # prev = sys.getsizeof(t)
# # for i in range(10):
# #     c = tuple(range(i+1))
# #     size_c = sys.getsizeof(c)

# #, [27.02.23 23:32]
# #     delta, prev = size_c - prev, size_c
# # delta = size_c - prev
# # prev = size_c
# # print(f'{i+1}: items: {size_c}, delta={delta}')
#
# # l = list()
# # prev = sys.getsizeof(l)
# # for i in range(10):
# #     c = list(range(i+1))
# #     size_c = sys.getsizeof(c)
# #     delta, prev = size_c - prev, size_c
# #     print(f'{i + 1}: items: {size_c}, delta={delta}')
# # c = list()
# # prev = sys.getsizeof(c)
# # print(f'0 items: {prev}')
# # for i in range(255):
# #     c.append(i)
# #     size_c = sys.getsizeof(c)
# #     delta, prev = size_c - prev, size_c
# #     print(f'{i+1} items: {size_c}, delta={delta}')
#
# # t = tuple(range(100_000))
# # l = list(t)
# # print(timeit('t[99_999]',globals=globals(),number=10_000_000))
# # print(timeit('l[99_999]',globals=globals(),number=10_000_000))
#
# # 7. Index Base and Slice Bounds - Rationale.
#
# # 8. Copying Sequences - Lecture.
#
# # s = [1,2,3,4]
# # cp = []
# # for e in s:
# #     cp.append(e)
# # print(s)
#
# # s = [10,20,30]
# # cp = s.copy()
# # print(s)
# # cp = s[0:len(s)]
# # print(cp)
# # cp = s[:]
# # print(cp)
#
# # l1 = [1,2,3]
# # l2 = list(l1)
# # print(id(l1),id(l2))
#
# # t1= (1,2,3,4)
# # t2=tuple(t1)
# # print(t1,t2)
# # print(id(t1),id(t2))
#
# # t1 = (1,2,3)
# # t2 = t1[:]
# # print(t1,t2)
#
# # s = [10,20,30]
# # cp = s.copy()
# # cp.append(100)
# # s.append(1000)
# # cp[0]=12
# # print(cp,s)
#
# # s = [ [10,20,30], [30,40] ]
# # cp = s.copy()
# # # cp[0]= 'python'
# # cp [0][0] = 'python'
# # print(cp)
#
# # s = [[0,0], [0,0]]
# # cp = [e.copy() for e in s]
# # print(cp)
#
# # a = [10, 20]
# # b = [a, 30]
# # a.append(b)
# # print(b)


### 9. Copying Sequences - Coding.
# # l1 = [1,1]
# # l2 = [2,2]
# # l3 = [3,3]
# # l4 = [4,4]
# # line1 = [l1, l2]
# # line2 = [l3, l4]
# # plane1 = [line1, line2]
# # plane2 = copy.deepcopy(plane1)
# # plane1[0][0][0] = 10
# # print(plane1)
# # print(plane2)
#
# # class Point:
# #     def init(self, x, y):
# #         self.x = x
# #         self.y = y
# #
# #     def repr(self):
# #         return f'Point({self.x},{self.y})'
# #
# #
# # class Line:
# #     def init(self, p1, p2):
# #         self.p1 = p1
# #         self.p2 = p2
# #
# #     def repr(self):
# #         return f'Line({self.p1.repr()},{self.p2.repr()})'
# #
# #
# # p1 = Point(0, 0)
# # p2 = Point(10, 10)
# # line1 = Line(p1, p2)
# # line2 = copy.deepcopy(line1)
# # print(line1.p1, id(line1.p1))
# # print(line2.p1, id(line2.p1))
# #
# # p1 = Point(0, 0)
# # p2 = Point(10, 10)
# # line1 = Line(p1, p2)
# # line2 = copy.copy(line1)
# # print(line1.p1, id(line1.p1))
# # print(line2.p1, id(line2.p1))


### 10. Slicing - Lecture.
# # l = [1,2,3,4,5]
# # print(l[0:2])
# # l[0:2]=('a','b','c')
# # print(l)
#
# # l = ['a','b','c','d','e','f','g']
# # print(l[3:100])
#
# # l = ['a','b','c','d','e','f']
# # print(l[-4:-3])
# # print(l[1:15:3])
# # print(l[-1:-4:-1])
# # print(l[0:100])
# # print(l[3:-1:-1])


### 11. Slicing - Coding.
# # s = slice(0, 2)
# # print(type(s))
# # print(s.start)
# # print(s.stop)
# # print(s.step)
#
# # l = [1,2,3,4,5]
# # print(l[2:3])
# # print(l[s])
#
# # l = 'python'
# # print(l[0:1])
# # print(l[1:1])
# # print(l[0:])
# # print(l[0:0])
# # print(l[0:6:2])
#
# # s1 = slice(None, 4)
# # print(l[False:6])
# # start = None
#
#
# # print(l[start:4])
# # print(l[3:0:-1])
# # s = slice(1,5)
# # print(s.start,s.stop,s.step)
# # print(s.indices(4))
# # print(s.indices(10))
# # print(list(range(1,5,1)))
# # print((slice(0,100,2).indices(6)))
# # print(list(range(0,10,2)))
# # t = slice(0,100,2).indices(10)
# # print(range(*t))
# # start = None
# # stop = None
# # step = -1
# # length = 10
# # print(list(range(*slice(start,stop,step).indices(length))))
# # print(l[::-1])

### 13.Custom Sequences - Part 1 - Lecture
# my_list = ['a','b','c','d','e','f','j']
# my_list.__getitem__(0) ##will take the 1st item in the lins 'a'
# my_list.__getitem__(2) ##will take the 3rd item in the lins 'c'
# my_list.__getitem__(-1) ##will take the last item in the lins 'j'
# my_list.__getitem__(slice(0, 4, 1)) ##will take the items from 'a' to 'd'
# my_list.__getitem__(100) ## will raise an IndexEror
#
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# index = 0
# while True:
#     try:
#         item = my_list.__getitem__(index)
#     except IndexError:
#         break
#     print(item)
#     index += 1
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# len(my_list) #>> count of items "10"
# my_list.__len__()  #>> count of items "10"


### 14. Custom Sequences - Part 1 - Coding
# fibonacci
# def fib(n):
#     if n < 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# f = fib(5)


### 15.In-Place Concatenation and Repetition - Lecture
##Concatenation +
##for example list
# l1 = [1, 2, 3, 4, 5]
# print(l1, id(l1))
# l2 = [6, 7, 8, 9, 10]
# print(l2, id(l2))
# l1 = l1 + l2
# print(l1, id(l1))
#
# #In-Place Concatenation +=
# #for example string (immutable)
# s1 = "hello"
# print(s1, id(s1))
# s2 = "world"
# print(s2, id(s2))
# s1 += s2
# print(s1, id(s1))
# for example lists (mutable)
# l1 = [1, 2, 3, 4, 5]
# print(l1, id(l1))
# l2 = [6, 7, 8, 9, 10]
# print(l2, id(l2))
# l1 += l2
# print(l1, id(l1)) #id of l1 dose not change
#
##In-Plase Repetition *=
# l1 = [1, 2, 3]
# l1 = l1 * 2 #id of l1 changes
#
# l1 *= 2 #id of l1 dose not change


### 17.Assignments in Mutable Sequences - Lecture
# l = [1, 2, 3, 4, 5]
# l[1:3] = [10, 20, 30]
# print(l)   # l = [1, 10, 20, 30, 4, 5] (ID of l did not change)
#
# l[1:4:2] = [10, 20]
# print(l)   # l = [1, 10, 3, 20, 5] (ID of l did not change)
#
#
# Deleting a slice
# l = [1, 2, 3, 4, 5]
# l[2:4] = []
# print(l)  #l = [1, 2, 5]  (ID of l did not change)
#
# l = [1, 2, 3, 4, 5]
# l[1:1] = 'abc'
# print(l)  # l = [1,  'a', 'b', 'c', 2, 3, 4, 5] (ID of l did not change)


### 19-22. Custom Sequences - Part 2
#
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'MyClass(name={self.name}'
#
#     def __add__(self, other):
#        return MyClass(self.name + other.name)
#
#     def __iadd__(self, other):
#         if isinstance(other, MyClass):
#             self.name += other.name
#         else:
#             self.name += other
#         return self
#
#     def __mul__(self, n):
#         return MyClass(self.name * n)
#
#     def __rmul__(self, n):
#         return self.__mul__(n)
#
#     def __imul__(self, n):
#         self.name *= n
#         return self
#
#     def __contains__(self, value):
#         return value in self.name
#
#
#
# c1 = MyClass('Mick')
# c2 = MyClass('Eric')
#
##FOR __add__
# print('ID of c1 is: ', id(c1))          #ID of c1 is:  139704373848400
# print('ID of c2 is: ', id(c2))          #ID of c2 is:  139704373850320
# result = c1 + c2
# print('ID of result is: ', id(result))  #ID of result is:  139704373849936
# print(result)                           #MyClass(name=MickEric
#
##FOR __iadd__
# print('ID of c1 is: ', id(c1))           #ID of c1 is:  140238413736272
# print('ID of c2 is: ', id(c2))           #ID of c2 is:  140238413738192
# c1 += c2
# print('ID of c1 is: ', id(c1))           #ID of c1 is:  140238413736272
# print(c1)                                #MyClass(name=MickEric
#
#
#
##FOR __mul__
# print('ID of c1 is: ', id(c1))          #ID of c1 is:  139986937669968
# result = c1 * 3
# print('ID of result is: ', id(result))  #ID of result is:  139986937670400
# print(result)                           #MyClass(name=MickMickMick
#
##FOR __imul__
# print('ID of c1 is: ', id(c1))           #ID of c1 is:  140676447971664
# c1 *= 3
# print('ID of c1 is: ', id(c1))           #ID of c1 is:  140676447971664
# print(c1)                                #MyClass(name=MickMickMick
#
#
#
##FOR __contains__
# c3 = MyClass('Python developer')
# print('Pyt' in c3)    #True
# print('loper' in c3)  #True
# print('Java' in c3)   #False
#
#
#
#
# from collections import namedtuple
# Point = namedtuple('Point', 'x y')
# p1 = Point(10.5, 3.2)
# print(p1)
# import numbers
#
#
# isinstance(10, numbers.Number)     #True
# isinstance('a', numbers.Number)    #False
# isinstance(10.32, numbers.Number)  #True
# isinstance(10+2j, numbers.Number)  #True
# isinstance(10+2j, numbers.Real)    #False
# isinstance(10, numbers.Real)       #True
#
# class Point:
#     def __init__(self, x, y):
#         if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
#             self._pt = (x, y)
#         else:
#             raise TypeError('Point co-ordinates must be real numbers. ')
#
#     def __repr__(self):
#         return f'Point(x={self._pt[0]}, y={self._pt[1]}'
#
#     def __len__(self):
#         return len(self._pt)
#
#     def __getitem__(self, s):
#         return self._pt[s]
#
#
#
# p1 = Point(10, 2.5)
# print(p1)         #Point(x=10, y=2.5
#
# p1 = Point('abc', 10)
# print(p1)        #Will raise TypeEror
#
# p1 = Point(10, 2)
# x, y = p1
#
# print(x)    #10
# print(y)    #2


### 23. Sorting Sequences - Coding
##sorted()
# t = 7, 4, 6, 3, 5, 2, 1
# sorted(t)   #will return sorted numbers in list
#
# s = {4,3,5,2,1,6,7,}
# sorted(s)   #will return sorted numbers in list
#
# d = {3:100, 2:300, 1:200}
# sorted(d)                       #will return sorted keys in list
# sorted(d, key=lambda k: d[k])   #will return keys based on the value
#
# t = 'hello', 'world', 'this', 'is', 'a', 'big', 'python', 'project'
# sorted(t)    #will return sorted words in list (based on the alpab. order (a,b,c,d))
#
##Sorting based on the length of strings
# def sort_key(s):
#   return len(s)
# sorted(t, key=sort_key)        #will return sorted words in list (based on the length of strings)
#
# sorted(t, key=lambda s: len(s))  #will return the same thing as with |def sort_key(s): |
#                                  # itll return sorted words in list (based on the length of strings)
#
#
##l.sort
# l = ['hello', 'world', 'this', 'is', 'a', 'big', 'python', 'project']
# l.sort()
# print(l)  # Mutates the list labelled by l (in-place sorting)
#
# l.sort(key=lambda s: len(s))
# print(l)
#
#
# import random
# random.seed(0)
# n = 10_000
# l=[random.randint(0, 1000) for n in range(n)]
#
# l.sort()
# print(l)


### 24. List Comprehensions
# squares = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         squares.append(i ** 2)
#
# print(squares)
#
# squares = [i ** 2 for i in range(1, 101) if i % 2 == 0]   #will return the same result
# print(squares)
#
#
##pascal's triangle
# from math import factorial
#
# def combo(n, k):
#     return factorial(n) // (factorial(k) * factorial(n-k))
#
# print(combo(4, 2))
#
#
# size = 10
# pascal = [[combo(n, k) for k in range(n + 1)] for n in range(size + 1)]
#
# print(pascal)
#
#
#
##Nested loop
# l1 = ['a', 'b', 'f', 'c', 'd', ]
# l2 = ['w', 'x', 'y', 'z', 'f']
#
# result = []
# for i in l1:
#     for j in l2:
#         if i != j:
#             result.append(i + j)
#
# print(result)
#
# result = [i + j for i in l1 for j in l2 if i != j]
# print(result)
#
##zip
#####
# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = ['a', 'b', 'c', 'd', 'f']
#
# print(list(zip(l1, l2)))
#
# result = []
#
# for index_1, item_1 in enumerate(l1):
#     for index_2, item_2 in enumerate(l2):
#         if index_1 == index_2:
#             result.append((item_1, item_2))
#
# print(result)   #will return the same result as the zip.
#
#
# l1 = [1, 2, 3, 4, 5, 6, 7]
# l2 = ['a', 'b', 'c', 'd', 'f']
# result = [[item_1, item_2] for index_1, item_1 in enumerate(l1) for index_2, item_2 in enumerate(l2) if index_1 == index_2]
# print(result)   #will return the same result as the zip.


#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
### Hash Maps(dict, set)
###dict
### 2-3. Creating Dictionaries
##   d = {key1: value1, key2: value2, key3: value3}   or  d = dict(key1=value1, key2=value2, key3=value3)
#
# d = {i: i ** 2 for i in range(1, 5)}
# print(d)  # {1: 1, 2: 4, 3: 9, 4: 16}
#
#
# d = {}
# for i in range(1, 5):
#     d[i] = i ** 2
# print(d)   #{1: 1, 2: 4, 3: 9, 4: 16}   #will return the same result
#
##############
##fromkeys()
# d = dict.fromkeys(['a', (0, 0), 100], 'N/A')
# print(d)      # {'a': 'N/A', (0, 0): 'N/A', 100: 'N/A'}
# d = dict.fromkeys((i ** 2 for i in range(1, 5)), False)
# print(d)        # {1: False, 4: False, 9: False, 16: False}
# d = dict.fromkeys('abcd', 0)
# print(d)          #{'a': 0, 'b': 0, 'c': 0, 'd': 0}
#
#################
##functions
#
# def fn_add(a, b):
#     r = a + b
#     return r
#
#
# def fn_inv(a):
#     return 1 / a
#
#
# def fn_mult(a, b):
#     return a * b
#
#
# d_func = {fn_add: (2, 3), fn_inv: (5), fn_mult: (3, 3)}
# print(d_func)
#
# d_func2 = {"add": fn_add(2, 3), "inv": fn_inv(5), "mult": fn_mult(3, 3)}
# print(d_func2)
###########
#
###########
# d = {'a': 123, 'b': [1, 2, 33, 4], 'c': {'aa': 222, 'bb': 333}}
# d_copy = dict(d)
#
# print(d, id(d))             #the result must be same but id not  ((   {'a': 123, 'b': [1, 2, 33, 4], 'c': {'aa': 222, 'bb': 333}}
#                             # 140006329804928
# print(d_copy, id(d_copy))   #the result must be same but id not  ((   {'a': 123, 'b': [1, 2, 33, 4], 'c': {'aa': 222, 'bb': 333}}
#                             #  140006329835968
#
#
# d_copy['c'] = 12333           #the value of 'c' must change in d_copy but not d
# print(d_copy)
#
#
#############
#
# keys = ['a', 'b', 'c']
# values = (1, 2, 3)
#
# d = {}
# for k, v in zip(keys, values):
#     d[k] = v
#
# print(d)     #d = {'a': 1, 'b': 2, 'c': 3}
###or
# d = {k: v for k,v in zip(keys, values)}
# print(d)      #d = {'a': 1, 'b': 2, 'c': 3}
#
#
###############
# x_coords = (-2, -1, 0, 1, 2)
# y_coords = (-2, -1, 0, 1, 2)
#
# grid = [(x, y) for x in x_coords for y in y_coords]          #[(-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2),........
#
# import math
# grid_extended = {(x, y): math.hypot(x, y) for x, y in grid}
# print(grid_extended)
################


### 4-5. Creating Dictionaries
#d = {'key1': 111, 'key2': 222}
##
#d['key3'] = 333
#
# print(d)     #{'key1': 111, 'key2': 222, 'key3': 333}
#
# print(d['key1'])  #111
# print(d['key45']) #KeyError:
#
##.get
# print(d.get('key1'))   #returns the value if key is found
# print(d.get('key45'))  #returns None if key is not found
###
# print('key1' in d)  #True if key is in d, False if is not
#
#
##removing elements from a Dictionary
##.clear
# d.clear()  #clearing out all items
# print(d)   #{}
####
#del d['key1']      #removes element with that key from d
#print(d['key1'])   #KeyError:
###
#d.pop('key1')      #removes element with that key from d and returns the corresponding value
###
#d.popitem()        #Python >= 3.6 removes last item
#
#####
#
# text = 'hello world: this is pyhton code'
# d_text = {}
# for i in text:
#     d_text[i] = d_text.get(i, 0) + 1
#
# print(d_text)
##############################


### 6-7. Dictionary Views
#
#
#d = {'key1': 111, 'key2': 222, 'key3': 333, 'key4': 444}
#
# print(d.keys())      #dict_keys(['key1', 'key2', 'key3', 'key4'])
# print(d.values())    #dict_values([111, 222, 333, 444])
# print(d.items())     #dict_items([('key1', 111), ('key2', 222), ('key3', 333), ('key4', 444)])
#
##Set operations
# s1 = {'a', 'b', 'c'}
# s2 = {'c', 'a', 'd'}
# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
############
# s1 = {'a': 1, 'b': 2, 'c': 3}
# s2 = {'c':5, 'a':6, 'd':7}
# print(s1.keys() | s2.keys())
# print(s1.keys() & s2.keys())
# print(s1.keys() - s2.keys())
#
################




### 8-9. Updating, Merging, and Copying
#
#
##d1.update(d2)
# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 20, 'c': 30}
# d1.update(d2)
# print(d1)      #{'a': 1, 'b': 20, 'c': 30}  #'b' was updated, 'c' was inserted
#########
##d1.update(keyword-args)
# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 20, 'c': 30}
# d1.update(b=2, c=30)
# print(d1)     #{'a': 1, 'b': 2, 'c': 30}
#######
##d1.update(iterable)
# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 20, 'c': 30}
# d1.update(((k, ord(k)) for k in 'bcd'))
# print(d1)        #{'a': 1, 'b': 98, 'c': 99, 'd': 100}
# d1.update(b=40, x=50, s=20)
# print(d1)          #{'a': 1, 'b': 40, 'x': 50, 's': 20}
#######
##Unpacking dictionaries
# d1 = {'a': 1, 'b': 2, 'd': 444}
# d2 = {'b': 20, 'c': 30, 'd':40}
#
# d = {**d1, **d2}
# print(d)        #{'a': 1, 'b': 20, 'd': 40, 'c': 30}
#########
##Copying Dictionaries
# d = {'b': 20, 'c': 30, 'd': 40}
##shallow copies
# copy_d = d.copy()
# copy_d = {**d}
# copy_d = dict(d)
# copy_d = {k:v for k, v in d.items()}
###







#####################################################################################################################
#####################################################################################################################
#####################################################################################################################



###Set
### 2. Basic Set Theory
# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# s3 = {6, 7, 8, 9, 10}
#
# s1 | s2 | s3           #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# s1.union(s2, s3)       #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
 ###
# s2 & s3                #{8, 6, 7}
# s2.intersection(s3)    #{8, 6, 7}
 ###
# s1 - s2               #{1, 2, 3}
# s1.difference(s2)     #{1, 2, 3}
 ###
# s1 ^ s2                     #{1, 2, 3, 6, 7, 8}
# s1.symmetric_difference(s2) #{1, 2, 3, 6, 7, 8}
 ###
 ###
##subset
# s1 = {1, 2, 3, 4}
# s2 = {1, 2, 3, 4, 5, 6}
# s3 = {1, 2, 3, 4}
# s1 <= s2          #True
# s1.issubset(s2)   #True
##proper subset
# s1 < s2          #True
# s1 < s3          #False
##superset
# s2 >= s1          #True
# s2.issuperset(s1) #true
##proper suberset
# s2 > s1           #True
#################




### 5. Creating Sets
# st1 = 'asdfggghjkkaaa'
# set1 = set(st1)
# print(set1)         #{'k', 'd', 'a', 'g', 'f', 'h', 'j', 's'}
###
# def scorer(s):
#     alphabet = set('abcdefghijkl')
#     s = s.lower()
#     dist = set(s)
#     effective = dist & alphabet
#     return len(effective), effective
# print(scorer('abczxxYf'))    #(4, {'f', 'b', 'a', 'c'})
##############



### 6. Common Operations
#
##Addind elements
# s = {1, 2, 3, 4, 5}
# s.add(6)
# print(s)       # {1, 2, 3, 4, 5, 6} (6 added to set)
#
#
##Removing elements
# s = {1, 2, 3, 4, 5}
# s.remove(3)
# print(s)        #{1, 2, 4, 5}  (3 was removed)
# s.remove(7)     #KeyError if the element does not exist
# s.discard(2)
# print(s)         #{1, 3, 4, 5}  (2 was removed)
# s.discard(7)     #if element does not exist returns the same result
# print(s)         #{1, 3, 4, 5}
#
# s.pop()           #removes and returns an arbitrary element
#
# s.clear()         #removes all elements from set
##########


### 10-11. Update Operations
##Analogous Set mutating updates  (|=, &=, -=, ^=)
#
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# s3 = {4, 5, 6, 7}
###
# print(s1, id(s1))        #{1, 2, 3, 4} 140033700340992
# print(s2, id(s2))        #{3, 4, 5, 6} 140033700341440
###
# s1 = s1 & s2
# print(s1, id(s1))        #{3, 4} 140513692166048  (the ID of s1 has changed)
###
# s1 &= s2
# print(s1, id(s1))        #{3, 4} 140033700340992 (the ID of s1 has not changed (s1 has mutated))
##or
# s1.intersection_update(s2)
# print(s1, id(s1))       #the same result::{3, 4} 140033700340992 (the ID of s1 has not changed (s1 has mutated))
#########
# s1 -= s2
# print(s1)                #{1, 2} ((s1 has mutated))
##
# s1 -= s2 - s3              #s1 - (s2 - s3)
# print(s1)                  #{1, 2, 4}  ((s1 has mutated))
##or
# s1.difference_update(s2, s3) #the same result
######
# s1 |= s2 | s3
# print(s1)                    #{1, 2, 3, 4, 5, 6, 7} ((s1 has mutated))
## or
# s1.update(s2, s3)            ##the same result
#####
# s1 ^= s2
# print(s1)                     #{1, 2, 5, 6}  ((s1 has mutated))
#
############



### 13. Copying Sets
# #
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'Person(name={self.name})'
#
# p1 = Person('John')
# p2 = Person('Sara')
#
# s1 = {p1, p2}
#
# s2_copy = s1.copy()
# s1 is s2_copy      #False
# s1 == s2_copy      #True
#
# s3_copy = {*s1}
# s1 is s3_copy      #False
# s1 == s3_copy      #True
#
# ##deep copy
# from copy import deepcopy
# s4_dpcopy = deepcopy(s1)
# s1 is s4_dpcopy    #False
# s1 == s4_dpcopy    #False
# ##
#
# print(s1, id(s1))                   #{Person(name=John), Person(name=Sara)} 140516324876224
# print(s2_copy, id(s2_copy))         #{Person(name=John), Person(name=Sara)} 140516324878464
# print(s3_copy, id(s3_copy))         #{Person(name=John), Person(name=Sara)} 140516324878240
# print(s4_dpcopy, id(s4_dpcopy))     #{Person(name=John), Person(name=Sara)} 140350100810528
#
# p1.name = 'Henry'
#
# print(s1, id(s1))                  #{Person(name=Henry), Person(name=Sara)} 140568488779712
# print(s2_copy, id(s2_copy))        #{Person(name=Henry), Person(name=Sara)} 140568488781952
# print(s3_copy, id(s3_copy))        #{Person(name=Henry), Person(name=Sara)} 140568488781952
# print(s4_dpcopy, id(s4_dpcopy))    #{Person(name=John), Person(name=Sara)}  140350100810528
#
# ####



### 14. Frozen Sets
#
#
# s1 = {'a', 'b', 'c'}
# print(type(s1), s1)      #<class 'set'> {'b', 'c', 'a'}
#
# frz_s = frozenset({'d', 'f', 'g'})
# print(type(frz_s), frz_s)  #<class 'frozenset'> frozenset({'g', 'd', 'f'})
####
#
# s1 = {1, 2, 3, 4}
# s2_copy = s1.copy()
# print(id(s1), s1)             #139799848625408 {1, 2, 3, 4}
# print(id(s2_copy), s2_copy)   #139799848624064 {1, 2, 3, 4}
###
# s1_frz = frozenset({1, 2, 3, 4})
# s2_frz_cp = frozenset(s1_frz)
# print(id(s1_frz), s1_frz)  # 139919830903136 frozenset({1, 2, 3, 4})
# print(id(s2_frz_cp), s2_frz_cp) #139919830903136 frozenset({1, 2, 3, 4})  the same ID
 ###


 #####################################################################################################################
 #####################################################################################################################
 #####################################################################################################################


###LOOPS
### 1. While loop
#
##example N1
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
##Output 0 1 2 3 4
####
#
##example N2
# i = 0
# while True:
#     print(i)
#     i += 1
#     if i > 5:
#         print('limit is 5:')
#         break
#
# ####Output 0 1 2 3 4 5 Limit is 5:

##example N3  (Names)
#
# min_length = 3
#
# name = input("ehter your name: ")
#
# while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
#     name = input("please try again: ")
#
# print(f"Hello {name}")
#
# #############
#
##example N4  (Names)
#
# min_length = 3
#
# while True:
#     name = input("ehter your name: ")
#     if len(name) >= min_length and name.isprintable() and name.isalpha():
#         break
# print(f"Hello {name}")
# #############
#
#
##example N5  while else:
# #
# l = [1, 2, 3, 4, 5]
# val = 7
# indx = 0
#
# while indx < len(l):
#     if l[indx] == val:
#         print('7 is there! ')
#         break
#     indx += 1
# else:
#     l.append(val)
#     print(f"{val} is appended to list: ")
#
# print(l)
#
# ##########
#
#




### 2. Break, Continue, and the Try Statement
#
# try:
#   print(x)
# except NameError:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
########
#
# a = 10
# b = 4
#
# while a > 0:
#     a -= 1
#     b -= 1
#     try:
#         r = a // b
#     except ZeroDivisionError:
#         print(":ZeroDivisionError:: ")
#     finally:
#         print(f'the result is {r}')
# else:
#     print('_______________')
#     print("end of loop!!!!")
#
########################################

### 3. The For Loop
#
# for i in [5, 4, 3, 2, 1]:
#     print(i)
#####
#
# for i in range(10):
#     print(i)
####
# for s in 'hello':
#     print(s)
######
# for i in range(1, 10):
#     print(i)
#     if i == 7:
#         print('7 is founded')
#         break
# else:
#     print("Done")
#####################################




 ######################################################################################################################
 ######################################################################################################################
 ######################################################################################################################

###Functions

### 1. Functions
#
# def func_1(a, b):
#     return a * b
#
#
# print(func_1(12, 2))
##############
#
# def func_3():
#     return func_4()
#
# def func_4():
#     print("asdasasd")
#
# func_3()
######
#
# def my_func(a, b=10, c=10):
#     print(a, b, c)
#
# my_func(12)                 #12 10 10
# my_func(20, 30, 40)         #20 30 40
# my_func(20, c=40)           #20 10 40
# my_func(b=40, c=50, a=12)   #12 40 50
#####

### 5. Unpacking Iterables
#
# a, b, c = 1, 2, 3
# print(a)   #1
# print(b)   #2
# print(c)   #3
# a, b, c = "XYZ"
# print(a)   #X
# print(b)   #Y
# print(c)   #Z
#  #####
# a = 10
# b = 20
# a,b = b ,a
# print(a)    #a = 20
# print(b)    #b = 10

####################



### 7. Extended Unpacking
## using  *
# l = [1,2,3,4,5]
# a, b = l[0], l[1:]   #we can achieve this using simple unpacking:
# print(a, b)          #a = 1   b = 2,3,4,5
#
# a, *b = l              #we can also use the * operator:
# print(a, b)            #a = 1   b = 2,3,4,5
# a, *b, c = l
# print(a, b, c)          #a = 1    b = 2, 3, 4     c = 5
####
## using **
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'d': 4, 'e': 5}
# d3 = {'f': 6, 'g': 7}
#
# d = {**d1, **d2, **d3}  #we can use ** to unpack dicts.
# print(d)                #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
#
## Nested Unpacking
# l = [1, 2, [3, 4]]
# a, b, (c, d) = l
# print(a, b, c, d)      # a = 1    b = 2    c = 3   d = 4



### 9-10. args
#
# def func1(a,b,*c):
#     print(a)
#     print(b)
#     print(c)
#
# func1(1, 2, 3, 3, 4)  #a = 1  b = 2  c = (3, 3, 4)
# func1(1, 2)      #a = 1  b = 2   c = ()
########
# def avg(*args):
#     count = len(args)
#     total = sum(args)
#     if count == 0:
#         return 0
#     else:
#         return total
#
# print(avg(1,2,3,4))    #10

####OR
#
# def avg(*args):
#     count = len(args)
#     total = sum(args)
#     return count and total    #if count is 0 returns 0(False and True --> returns False),  and if count great then 0 returns total
#
# print(avg())           #0
# print(avg(1,2,3,4))    #10
################
# def func2(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
#
# l = [10, 20, 30]
#
# # func2(l)    #TypeError
# func2(*l)     # 10 20 30
#
##############################




### 11. Keyword Arguments
# def myfunc(a, b, *c, d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
#
# myfunc(12, 23, 45, 56, 67, d=777)      #a = 12  b = 23  c = (45, 56, 67)  d = 777
####
# def myfunc_2(*a, b):
#     print(a)
#     print(b)
#
# myfunc_2(1, 2)      #TypeError:
# myfunc_2(1, b=2)      #  a = (1,)  b = 2
#
####
# def func_3(*, d):
#     print(d)
#
# func_3(11)       #TypeError
# func_3(d=11)     #11
####
# def func_4(a, b, *, d):
#     print(a)
#     print(b)
#     print(d)
#
# func_4(1, 2, 3, d=4)      #TypeError
# func_4(1, 2, d=4)           #a = 1  b = 2  d = 4
##########




### 13. Kwargs
#
# def func(**kwargs):
#     print(kwargs)
# func(a = 12, b = 34, c = 45)     #kwargs = {'a': 12, 'b': 34, 'c': 45}
# func()                           #kwargs = {}
#
# def func(*, d, **kwargs):
#     print(d)
#     print(kwargs)
# func(d = 11, x = 5, y = 6, z = 7)      # d = 11   kwargs = {'x': 5, 'y': 6, 'z': 7}
# func(d = 11)                           # d = 11   kwargs = {}
#
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# func(1, 2, 3, 4, a=5, b=6, c=7)         #  args = (1, 2, 3, 4)   kwargs = {'a': 5, 'b': 6, 'c': 7}
#
#
# def func(a, b, *, d, **kwargs):
#     print(a)
#     print(b)
#     print(d)
#     print(kwargs)
#
# func(1, 2, x=33, y=44, s = 66, z=55, d=8)      # a = 1  b = 2  d = 8  kwargs = {'x': 33, 'y': 44, 's': 66, 'z': 55}




### 16. Lambda Expressions
#
# myfunc = lambda x: print(x**2)
#
# myfunc(4)
#
#####
# def test_func(x, func):
#     return func(x)
#
# test_func(3, lambda x: x**2)          #returns 9 (3**2)
# test_func(5, lambda x: x * 2 + 10)    #returns 20 (5 * 2 + 10)
##########




### 18. Lambdas and Sorting
# d = {'a': 40, 'b': 30, 'c': 10, 'd': 20}
#
# print(sorted(d))                       #['a', 'b', 'c', 'd']  ((sorting by keys
# print(sorted(d, key=lambda x: d[x]))   #['c', 'd', 'b', 'a']   (sorting by values
 #####
# l = ['Nike', 'Fila', 'Adidas', 'New Balance']
#
# print(sorted(l))                         #['Adidas', 'Fila', 'New Balance', 'Nike']  ((sorted by first letters
# print(sorted(l, key=lambda s: s[-1]))    #['Fila', 'Nike', 'New Balance', 'Adidas']    ((sorted by last letters
#
##################



### 20. Map, Filter, Zip, and List Comprehensions
## the map function
# l = [1, 2, 3, 4, 5]
#
# def sq(x):
#     return x ** 2
#
# l1 = list(map(sq, l))  # will return [1, 4, 9, 16, 25]
#
####
#
## the filter function
# l = [0, 1, 2, 3, 4, 5]
# list(filter(None, l))     #will return [1, 2, 3, 4, 5]   (0 is Falsy)
###
# l = [0, 1, 2, 3, 4, 5]
#
# def is_even(n):
#     return n % 2 == 0
#
# list(filter(is_even, l))   #will return [0, 2, 4]
#
## the zip function
# l1 = [1,2,3,4]
# l2 = [10,20,30,40]
# l3 = 'abcd'
#
# list(zip(l1,l2,l3))       #[(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c'), (4, 40, 'd')]
#####
#
##List Comprehensions
# l = [2, 3, 4]
#
# l1 = [x ** 2 for x in l]
# print(l1)       # [4, 9, 16]
##
# l1 = [1, 2, 3]
# l2 = [10, 20, 30]
#
# l3 = [x + y for x, y in zip(l1, l2)]
# print(l3)        #[11, 22, 33]
#
##Combining map and filter
# l = range(10)
#
# l2 = list(filter(lambda a: a % 2 == 0, map(lambda x: x**2, l)))
# print(l2)         #[0, 4, 16, 36, 64]
#
##############







######################################################################################################################
######################################################################################################################
######################################################################################################################


### Decorators

### 2. Decorators(Part 1)
#
# def counter(fn):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'function {fn.__name__} was called {count} times')
#         result = fn(*args, **kwargs)
#         return result
#     return inner
#
###
# def add(a, b):
#     return a + b
#
# add = counter(add)
# print(add(13, 3))       #function add was called 1 times  16
# print(add(2,3))         #function add was called 2 times 5
#
###
# def mult(a, b, c,):
#     return a * b * c
# print(mult(2,3,1))     # 6
# mult = counter(mult)
# print(mult(2, 3, 1))     #function mult was called 1 times   6
#
###
### @ Symbol
# @counter             # use @counter instead of minus = counter(minus)
# def minus(x, y):
#     return x - y
#
# print(minus(5, 2))     #function minus was called 1 times   3
#
##############################



### 3. Decorator Application (Timer)
#
#
# def timeer_decorator(fn):
#     from datetime import datetime
#     from functools import wraps
#
#     @wraps(fn)
#     def inner(*args, **kwargs):
#         start = datetime.now()
#         result = fn(*args,**kwargs)
#         stop = datetime.now()
#         elapsed = stop - start
#
#
#         args_ = [str(a) for a in args]
#         kwargs_ = [f'{k}={v}' for (k, v) in kwargs.items()]
#         all_args = args_ + kwargs_
#         args_str = ','.join(all_args)
#
#         print(f'{fn.__name__} {args_str} took {elapsed}s to run.')
#
#         return result
#     return inner
#
##fibonacci
# @timeer_decorator
# def rec_fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return rec_fib(n-1) + rec_fib(n-2)
#
#
# print(rec_fib(5))
#
##fibonacci loop
# @timeer_decorator
# def fib_loop(n):
#     fib_1 = 1
#     fib_2 = 1
#     for _ in range(3, n+1):
#         fib_1, fib_2 = fib_2, fib_1+fib_2
#     return fib_2
#
#
# print(fib_loop(5))

#######################



### 4. Decorator Application (Logger, Stacked Decorators)
#
# # logged decorator
# def logged(fn):
#     from functools import wraps
#     from datetime import datetime, timezone
#
#     @wraps(fn)
#     def inner(*args, **kwargs):
#         run_dt = datetime.now(timezone.utc)
#         result = fn(*args, **kwargs)
#         print(f'{run_dt}: called {fn.__name__}')
#         return result
#     return inner
#
# # timer decorator
# def timeer_decorator(fn):
#     from datetime import datetime
#     from functools import wraps
#
#     @wraps(fn)
#     def inner(*args, **kwargs):
#         start = datetime.now()
#         result = fn(*args,**kwargs)
#         stop = datetime.now()
#         elapsed = stop - start
#
#         print(f'{fn.__name__} run for {elapsed}s::')
#
#         return result
#     return inner
#
# # factorial function  with 2 decorator
# @timeer_decorator
# @logged
# def fuct(n):
#     from operator import mul
#     from functools import reduce
#
#     return reduce(mul, range(1,n+1))
#
#
# print(fuct(4))
#




### 7. Decorators (Part 2)
#
# def timed(fn, reps):
#     from time import perf_counter
#
#     def inner(*args, **kwargs):
#         total_elap = 0
#         for i in range(reps):
#             start = perf_counter()
#             result = fn(*args, **kwargs)
#             end = perf_counter()
#             total_elap += (end - start)
#
#         avg_run_time = total_elap / reps
#         print(f'Avg run time: {avg_run_time}s:{reps} reps:')
#         return result
#     return inner
#
#
# ##fibonacci function
# def calc_fib_recurse(n):
#     return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)
#
#
# ## @timed(10) #this is not going to be work
# def fib(n):
#     return calc_fib_recurse(n)
#
# fib = timed(fib, 10)
#
# print(fib(7))
#
#####
######################
## factory decarator
#
# def def_factory(reps):
#     def timed(fn):
#         from time import perf_counter
#
#         def inner(*args, **kwargs):
#             total_elap = 0
#             for i in range(reps):
#                 start = perf_counter()
#                 result = fn(*args, **kwargs)
#                 end = perf_counter()
#                 total_elap += (end - start)
#
#             avg_run_time = total_elap / reps
#             print(f'Avg run time: {avg_run_time}s:{reps} reps:')
#             return result
#         return inner
#     return timed
#
# ##fibonacci function
# def calc_fib_recurse(n):
#     return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)
#
#
# @def_factory(10) #now it going to be work
# def fib(n):
#     return calc_fib_recurse(n)
#
# print(fib(7))
#
########################################




### 1. Decorator Application (Decorator Class)
## example of Decorator Class
# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __call__(self, fn):
#         def inner(*args, **kwargs):
#             print(f'decarater function called: a={self.a}, b={self.b} ')
#             return fn(*args,**kwargs)
#
#         return inner
#
# @MyClass(10, 20)
# def my_func(s):
#     print(f'runing my_func: argument={s}')
#
# my_func(5)
#
#####################################





### 2.Decorator Application (Decorating Classes)
#
# from datetime import datetime, timezone
#
# def info(self):
#     results = []
#     results.append(f'time: {datetime.now(timezone.utc)}')
#     results.append(f'Class: {self.__class__.__name__}')
#     results.append(f'ID: {hex(id(self))}')
#     for k, v in vars(self).items():
#         results.append(f'{k}:{v}')
#     return results
#
# def debug_info(cls):
#     cls.debag = info
#     return cls
#
# @debug_info
# class Person:
#     def __init__(self, name, birth_year):
#         self.name = name
#         self.birth_year = birth_year
#
#     def say_hi():
#         return 'Hello there!'
#
# # p = Person('AKA', 1999)
# # print(p.debag())      #['time: 2023-03-31 16:28:12.863710+00:00', 'Class: Person', 'ID: 0x7f7e6555a950', 'name:AKA',
#                         # 'birth_year:1999']
#
#
# @debug_info
# class Auto:
#     def __init__(self, make, model, year, top_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.top_speed = top_speed
#         self.speed = 0
#
#     @property
#     def speed(self):
#         return self._speed
#
#     @speed.setter
#     def speed(self, new_speed):
#         if new_speed > self.top_speed:
#             raise ValueError("Speed can't exceed top_speed.")
#         else:
#             self._speed = new_speed
#
# favorite = Auto('Ford', 'Model T', 1908, 45)
#
# print(favorite.debag())


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################




### Iterators

### 2. Iterating Collections

# class Squares:
#     def __init__(self):
#         self.i = 0
#
#     def next_1(self):
#         res = self.i ** 2
#         self.i+=1
#         return res
#
# sq = Squares()
#
# print(sq.next_1())   #0
# print(sq.next_1())   #1
# print(sq.next_1())   #4
# print(sq.next_1())   #9
# print(sq.next_1())   #16
#
##or with loops
#
# for i in range(5):
#     print(sq.next_1())
#
###
### StopIteration
#
# class Squares:
#     def __init__(self, lenght):
#         self.lenght = lenght
#         self.i = 0
#
#     def __len__(self):
#         return self.lenght
#
#     def __next__(self):
#         if self.i >= self.lenght:
#             raise StopIteration
#         else:
#             res = self.i ** 2
#             self.i+=1
#             return res
#
# sq = Squares(4)
#
# print(sq.__next__()) #  0
# print(sq.__next__()) #  1
# print(sq.__next__()) #  4
# print(sq.__next__()) #  StopIteration

# sq = Squares(10)
#
# while True:
#     try:
#         print(sq.__next__())
#     except StopIteration:
#         break
#
#
# class RandomNumber:
#     import random
#     def __init__(self, len, *, range_min=0,range_max=10):
#         self.len = len
#         self.range_min = range_min
#         self.range_max = range_max
#         self.num_requested = 0
#
#     def __len__(self):
#         return self.len
#
#     def __next__(self):
#         if self.num_requested >= self.len:
#             raise StopIteration
#         else:
#             self.num_requested += 1
#             return random.randint(self.range_min, self.range_max)
#
# r_num = RandomNumber(3)
#
# print(next(r_num))   #random numb
# print(next(r_num))   #random numb
# print(next(r_num))   #random numb
# print(next(r_num))   #StopIteration



### 4. Iterators - Coding
# class Squares:
#     def __init__(self, lenght):
#         self.lenght = lenght
#         self.i = 0
#
#     def __len__(self):
#         return self.lenght
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i >= self.lenght:
#             raise StopIteration
#         else:
#             res = self.i ** 2
#             self.i+=1
#             return res
#
#
# sq = Squares(4)
#
# print(list(enumerate(sq)))  #[(0, 0), (1, 1), (2, 4), (3, 9)]
#
# print(sq.__next__())   #StopIteration




### 6. Iterators and Iterables - Coding
#
# # creating a simple class
# class Cities:
#     def __init__(self):
#         self.cities = ['Paris', 'Barcelona', 'LA', 'London', 'Yerevan']
#         self.index = 0
#
#     def __len__(self):
#         return len(self.cities)

# ## creating a simple iterator
# class CityIterator:
#     def __init__(self, cities_obj):
#         self.cities_obj = cities_obj
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.cities_obj):
#             raise StopIteration
#         else:
#             item = self.cities_obj.cities[self.index]
#             self.index+=1
#             return item
#
#
# city_iterator = CityIterator(Cities())
#
# for city in city_iterator:
#     print(city)                #should print all cities in Cities class
#
# print(next(city_iterator))    #should rise a StopIteration error
#
#
#
# city_iterator = CityIterator(Cities())
#
# print(next(city_iterator))    #should return first city in Cities class
#
#
####
####
# creating a simple iterator
# class CityIterator:
#     def __init__(self, cities_obj):
#         self.cities_obj = cities_obj
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.cities_obj):
#             raise StopIteration
#         else:
#             item = self.cities_obj.cities[self.index]
#             self.index+=1
#             return item
#
# # creating a simple iterable
# class Cities:
#     def __init__(self):
#         self.cities = ['Paris', 'Barcelona', 'LA', 'London', 'Yerevan']
#         self.index = 0
#
#     def __len__(self):
#         return len(self.cities)
#
#     def __iter__(self):
#         return CityIterator(self)
#
#
#
# cities = Cities()
#
# for city in cities:
#     print(city)    ##should print all cities in Cities class
#
# ## we can do that again
# for city in cities:
#     print(city)    ##should print all cities in Cities class
#

######
######


### 8. Example 2 - Cyclic Iterators
#
# class CyclicIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         result = self.lst[self.i % len(self.lst)]
#         self.i +=1
#         return result
#
# iter_cycl = CyclicIterator('NSWE')
#
# nums = range(10)
#
# print(list(zip(list(nums), iter_cycl)))     #[(0, 'N'), (1, 'S'), (2, 'W'), (3, 'E'), (4, 'N'), (5, 'S'), (6, 'W'),
#                                             # (7, 'E'), (8, 'N'), (9, 'S')]
#
# iter_cycl = CyclicIterator('NSWE')
#
# n = 10
#
# for i in range(1, n+1):
#     direction = next(iter_cycl)
#     print(f'{i}{direction}')    #1N 2S 3W 4E 5N 6S 7W 8E 9N 10S
#
# items = [str(i) + next(iter_cycl) for i in range(1, n+1)]
# print(items)                   #['1W', '2E', '3N', '4S', '5W', '6E', '7N', '8S', '9W', '10E']
#
#
#
#
# #########
#########




### 10. Lazy Iterables - Coding
# import math
#
#
# class Circle:
#     def __init__(self, r):
#         self.radius = r
#         self._area = None
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, r):
#         self._radius = r
#         self._area = None
#
#     @property
#     def area(self):
#         if self._area is None:
#             print("Calculating area::")
#             self._area = math.pi * (self.radius ** 2)
#         return self._area
#
#
# c = Circle(2)
#
# print(c.area)
# print(c.area)
#####################
###################
#
# import math
#
#
# class Factorials:
#     def __init__(self, lenght):
#         self.lenght = lenght
#
#     def __iter__(self):
#         return self.FactIter(self.lenght)
#
#     class FactIter:
#         def __init__(self, lenght):
#             self.lenght = lenght
#             self.i = 0
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self.i >= self.lenght:
#                 raise StopIteration
#             else:
#                 res = math.factorial(self.i)
#                 self.i += 1
#                 return res
#
#
# facts = Factorials(5)
#
# print(list(facts))     #[1, 1, 2, 6, 24]





### 12. Python's Built-In Iterables and Iterators - Coding
#
# ## range
# r = range(10)
#
# print('__iter__' in dir(r))   #True
# print('__next__' in dir(r))   #False
# """ so range object is iterable"""
#
# """we can use that multipul times"""
# for num in r:
#     print(num)
#
# for num in r:
#     print(num)
#
# print([num for num in r])
#
#
## zip
# z = zip([1,2,3], 'abc')
#
# print('__iter__' in dir(z))   #True
# print('__next__' in dir(z))   #True
# """ zip is a iterator: """
#
# """we can use it only one time"""
# print(list(z))              #[(1, 'a'), (2, 'b'), (3, 'c')]
# print(list(z))              #[]
#
#
## open
# f = open('Games.py')
# print('__iter__' in dir(f))   #True
# print('__next__' in dir(f))   #True
# """ open object is a iterator: """
#
# """we can use f only one time"""
# for line in f:
#     print(line)
#
# for line in f:
#     print(line)
#
#
# """or we can do 'with open(file_name) as f' :"""
# with open('Games.py') as f:
#     for row in f:
#         print(row, end='')
#
#
# """we can also do it with 'redline':
#     but this way not recomended;
#     it gonna append all lines in list 'l' """
# with open('Games.py') as f:
#     l = f.readlines()
#
# print(l)





### 18. Example 3 - Delegating Iterators
#
# from collections import namedtuple
#
# Person = namedtuple('Person', 'first last')
#
# class PersonName:
#     def __init__(self, persons):
#         try:
#             self._persons = [person.first.capitalize() + ' ' + person.last.capitalize() for person in persons]
#         except (TypeError, AttributeError):
#             self._persons = []
#
#     def __iter__(self):
#         return iter(self._persons)
#
#
# persons = [Person('micheaL', 'palin',), Person('john', 'Wick'), ]
#
# person_names = PersonName(persons)
# print(person_names._persons)         #['Micheal Palin', 'John Wick']
#
# for i in person_names:
#     print(i)





########################################################################################################################
########################################################################################################################
########################################################################################################################



### Generators

### 2,3. Yielding and Generator Functions
#
# def my_func():
#     print('line 1')
#     yield 'Flying'
#     print('line 2')
#     yield 'Circus'
#
# print(type(my_func))    #<class 'function'>
#
# f = my_func()
# print(type(f))         #<class 'generator'>
#
# a = next(f)              #line 1
# print(a)                 #Flying
#
# b = next(f)              #line 2
# print(b)                 #Circus
###
#
# def silly():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
# s = silly()
#
# for i in s:
#     print(i)
#
####
##################




### 3. Example - Fibonacci Sequence
#
# ##fibonacci recursive
#
# def fib_rec(n):
#     if n <= 1:
#         return 1
#     else:
#         return fib_rec(n-1) + fib_rec(n-2)
#
# print([fib_rec(i) for i in range(50)])       #[1, 1, 2, 3, 5, 8, 13]
#
#
## fibonacci generator
#
# def fib(n):
#     fib_0 = 1
#     yield fib_0
#     fib_1 = 1
#     yield fib_1
#     for i in range(n-2):
#         fib_0, fib_1 = fib_1, fib_0 + fib_1
#         yield fib_1
#
# f = fib(7)
# for i in f:
#     print(i)
#
#
# ########





### 5. Making an Iterable from a Generator
#
# def squares_gen(n):
#     for i in range(n):
#         yield i**2
#
# sq = squares_gen(5)
#
# """so we can use it only ones"""
# for i in sq:
#     print(i)   #0 1 4 9 16
#
# for j in sq:
#     print(j)  # None
#
###
# """we need to make iterable"""
# def squares_gen_1(n):
#     for i in range(n):
#         yield i**2
#
# class Squares:
#     def __init__(self, n):
#         self.n = n
#     def __iter__(self):
#         return squares_gen_1(self.n)
#
#
# """or we can do it this way"""
# class Squares:
#     def __init__(self, n):
#         self.n = n
#     def __iter__(self):
#         return squares_gen_1(self.n)
#
#     @staticmethod
#     def squares_gen_1(n):
#         for i in range(n):
#             yield i ** 2
#
#
# """now we can use it more then one time"""
#
# sq = Squares(5)
# for i in sq:
#     print(i)    #0 1 4 9 16
#
# for i in sq:
#     print(i)    #0 1 4 9 16
#
#
######################
######################
######################



### 8. Generator Expressions and Performance
# """simple geneator expressions"""
# g = (i**2 for i in range(5))
#
# print(type(g))        #<class 'generator'>
#
# for item in g:
#     print(item)
#
####
# start = 1
# stop = 10
#
# mult_list_gen = ((i * j for i in range(start, stop+1))
#                         for j in range(start, stop+1))
#
# for line in mult_list_gen:
#     for item in line:
#         print(item, end=" ")
#     print('')
#
#
# #
# ###################
##############





#######################################################################################################################
#######################################################################################################################
#######################################################################################################################



### Modules, Packages and Namespaces

### 4. Imports and import lib
#
# ## Example 1
# # mod_name = 'math'
# # import mod_name       # ModuleNotFoundError:
#
# import importlib
# import sys
#
# importlib.import_module('math')
#
# print('math' in sys.modules)     # True
#
# # print(math.sqrt(2))           # NameError:
# """because 'math' is not in globals() """
# print('math' in globals())      #False
# ###
# math2 = importlib.import_module('math')
# print('math2' in globals())      #True
# print(math2.sqrt(2))           # 1.4142135623730951






### 9. Modules Recap
## importing build-in module
# import math
# print(type(math))        # <class 'module'>
# print(math.__spec__)     # ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')
# print(math.__name__)     # math
# print(math.__package__)  # ''
# """__file__ is not an atribute of math   (build-ins only)  """
#
####
# ## importing standard librarys
# import fractions
# print(type(fractions))        # <class 'module'>
# print(fractions.__spec__)     # ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader
#                               # object at 0x7f79be5f76d0>, origin='/usr/lib/python3.10/fractions.py'))
# print(fractions.__name__)     # fractions
# print(fractions.__package__)  # ''
# print(fractions.__file__)     #/usr/lib/python3.10/fractions.py
#
####
## importing castom module
# import test
# print(type(test))        # <class 'module'>
# print(test.__spec__)     # ModuleSpec(name='test', loader=<_frozen_importlib_external.SourceFileLoader
#                          # object at 0x7fbf5fa576d0>, origin='/home/kerimyan/PycharmProjects/pythonProject/test.py')
# print(test.__name__)     # test
# print(test.__package__)  # ''
# print(test.__file__)     #/home/kerimyan/PycharmProjects/pythonProject/test.py
#
###########################





#######################################################################################################################
#######################################################################################################################
#######################################################################################################################



### 2. Context Managers - Coding
#
# """it will create a new file and write to it"""
# with open('test.txt', 'w') as f:
#     f.writelines('This is a new test file ')
#
# with open('test5.txt') as f:
#     l = next(f)
#
# print(l)      #'This is a new test file '
#
##.....



### 3. Caveat when used with Lazy Iterators
# import csv
#
# def read_data():
#     with open('test.csv') as f:
#         yield from csv.reader(f, delimiter=',', quotechar='"')
#
# reader = read_data()
# print(type(reader))     #<class 'generator'>
#
#
# for row in reader:
#     print(row)
#
# """or we can do this..."""
# for _ in range(2):
#     print(next(reader))
####



### 4. Not just a Context Manager
#
# class DataIterator:
#     def __init__(self, fname):
#         self._fname = fname
#         self._f = None
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         row = next(self._f)
#         return row.strip('/n').split(',')
#
#     def __enter__(self):
#         self._f = open(self._fname)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if not self._f.closed:
#             self._f.close()
#         return False
#
#
# with DataIterator('test.csv') as data:
#     for row in data:
#         print(row)
#
####################



### 6. Additional Uses - Coding
#
### Change-reset context
# import decimal
#
# class Precision:
#     def __init__(self, prec):
#         self._prec = prec
#         self.real_prec = decimal.getcontext().prec
#
#     def __enter__(self):
#         decimal.getcontext().prec = self._prec
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         decimal.getcontext().prec = self.real_prec
#         return False
#
# with Precision(3):
#     print(decimal.Decimal(1) / decimal.Decimal(3))      # 0.333
#
# print(decimal.Decimal(1) / decimal.Decimal(3))          # 0.3333333333333333333333333333
#
# #####
# """But in fact decimal has a context manager"""
# """It will work the same vay!"""
# with decimal.localcontext() as ctx:
#     ctx.prec = 3
#     print(decimal.Decimal(1) / decimal.Decimal(3))      # 0.333
#
# print(decimal.Decimal(1) / decimal.Decimal(3))          # 0.3333333333333333333333333333
#
#
### Timer context manager
# from time import perf_counter, sleep
# class Timer:
#     def __init__(self):
#         self.elapsed = 0
#
#     def __enter__(self):
#         self.start = perf_counter()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.stop = perf_counter()
#         self.elapsed = self.stop - self.start
#         return False
#
# with Timer() as timer:
#     sleep(2)
#
# print(timer.elapsed)        # 2.000678701002471
#
#
######
#
### List marek context manager
#
# class ListMaker:
#     def __init__(self, title, prefix='-- ', indent=3):
#         self.title = title
#         self.prefix = prefix
#         self.indent = indent
#         self.courrent_indent = 0
#         print(title)
#
#     def __enter__(self):
#         self.courrent_indent += self.indent
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.courrent_indent -= self.indent
#         return False
#
#     def line_pr(self, arg):
#         s = ' ' * self.courrent_indent + self.prefix + str(arg)
#         print(s)
#
# with ListMaker('-TITLE-') as lm:
#     lm.line_pr('Line 1')
#     lm.line_pr('Line 2')
#     with lm:
#         lm.line_pr('Sub-Line 1')
#         lm.line_pr('Sub-Line 2')
#
#
#
###################



######################################################################################################################
######################################################################################################################
######################################################################################################################





### OOP

### 6. Class Attributes - Coding
#
# class Program:
#     language = 'Python'
#     version = '3.6'
#
# print(type(Program))     # <class 'type'>
###
# """Get attribute"""
# print(Program.language)   # Python
# print(Program.version)    # 3.6
# '''we can also use functions'''
# print(getattr(Program, 'language'))   # Python
# print(getattr(Program, 'version'))    # 3.6
#
# '''if attribute does not exist....'''
#
## print(getattr(Program, 'x'))         # AttributeError:
# print(getattr(Program, 'x', 'D/A'))         # D/A
####
# """Set attribute..."""
#
# Program.version = '3.8'
# print(Program.version)    # 3.8
# '''or with function 'setattr()' ...'''
# setattr(Program, 'version', '3.10')
# print(Program.version)   # 3,10
#
###
# """Remove attribute..."""
#
# del Program.version
# '''or with function 'delattr()' ...'''
# delattr(Program, 'version')
######
# print(Program.__dict__)  # {'__module__': '__main__', 'language': 'Python',
                         # 'version': '3.6', '__dict__': <attribute '__dict__' of 'Program' objects>,
                         # '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None}


################




### 8. Callable Class Attributes - Coding
#
# class Program:
#     language = 'Python'
#
#     def say_hello():
#         print(f'Hello from {Program.language}')
#
#
# print(Program.say_hello())      #Hello from Python
# print(getattr(Program, 'say_hello')())   #Hello from Python
# #or
# my_func = Program.say_hello
# print(my_func())      #Hello from Python

####



### 12. Data Attributes - Coding
# class BankAccount:
#     apr = 1.2
#
# acc_1 = BankAccount()
# acc_2 = BankAccount()
#
# print(acc_1 is acc_2)    # False
#
# print(acc_1.__dict__)   # {}
# print(acc_2.__dict__)   # {}
#
# print(acc_1.apr)      # 1.2
# print(acc_2.apr)      # 1.2
# """It first looks for it in the instance attribute ('acc_1.__dict__')
# then in the class attribute ('BankAccount.__dict__') ...'"""
#
#
# acc_1.apr = 0
# print(acc_1.__dict__)   # {'apr': 0}
# print(acc_2.__dict__)   # {}
# print(acc_1.apr)      # 0
# print(acc_2.apr)      # 1.2
#
# ###
# print(type(BankAccount.__dict__))     # <class 'mappingproxy'>
# print(type(acc_2.__dict__))           # <class 'dict'>
# """Type of 'acc_1.__dict__' is not 'mappingproxy' it's 'dict', so we can manipulate it..."""
# ## Example
# acc_2.__dict__['apr'] = 3
# print(acc_2.apr)   # 3
#
#
#####



### 14. Function Attributes - Coding
#
# class Person:
#     name = "A"
#
#     def say_hello(obj):
#         print(f'Hello from {a.name}')
#
#     def set_name(ins_obj, new_name):
#         ins_obj.name = new_name
#
# a = Person()
# print(type(Person.say_hello))     #<class 'function'>
# print(type(a.say_hello))          #<class 'method'>
# print(a.__dict__)                 # {}
# print(a.say_hello())              # Hello from A
#
# a.set_name('Karlenchik')          # or -->  Person.set_name(p, 'Karlenchik')
# print(a.__dict__)                 # {'name': 'Karlenchik'}
# print(a.say_hello())              # Hello from Karlenchik
#





### 16. Initializing Class Instances - Coding
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
# p = Person('Jhon')
# print(p.__dict__)      # {'name': 'Jhon'}
# print(p.name)          # Jhon
#
#
#



### 18.Creating Attributes at Run-Time - Coding
# from types import MethodType
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# p1 = Person('Eric')
# p2 = Person('Alex')
#
# print(p1.__dict__, p2.__dict__)     #{'name': 'Eric'} {'name': 'Alex'}
#
# p1.say_hello = MethodType(lambda self: f'{self.name} says hello:', p1)
#
# print(p1.__dict__)   #{'name': 'Eric', 'say_hello': <bound method <lambda> of <__main__.Person object at 0x7efdc3f3a860>>}
# print(p2.__dict__)   #{'name': 'Alex'}
# print(p1.say_hello())    # Eric says hello:
# ################
#
# from types import MethodType
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def register_do_work(self, func):
#         setattr(self, '_do_work', MethodType(func, self))
#
#     def do_work(self):
#         do_work_method = getattr(self, '_do_work', None)
#
#         if do_work_method:
#             return do_work_method()
#         else:
#             raise AttributeError('You must first register a do_work method::')
#
#
# math_t = Person('Vazgush')
# Phisic_t = Person('Varazdat')
#
# def work(self):
#     return f'{self.name} will do work::'
#
#
# # print(math_t.do_work())     # AttributeError: You must first register a do_work method::
#
# math_t.register_do_work(work)
#
# print(math_t.do_work())     # Vazgush will do work::
#
#


### 20. Properties - Coding
# class Person:
#     def __init__(self, name):
#         self.set_name(name)
#         """Instead useing 'self._name = name' we use ' self.set_name(name)' for seting name"""
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, value):
#         if isinstance(value, str) and len(value.strip())> 0:
#             self._name = value.strip()
#         else:
#             raise ValueError
#
#
# # p = Person(100)  #ValueError
#
# p = Person('AK')
# print(p.get_name())  # AK
# p.set_name('Eric')
# print(p.get_name())
#########
#
# # """Property"""
#
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, value):
#         if isinstance(value, str) and len(value.strip())> 0:
#             self._name = value.strip()
#         else:
#             raise ValueError
#
#     def del_name(self):
#         del self._name
#
#     name = property(fget=get_name, fset=set_name, fdel=del_name)
#
#
# p = Person('John')
# print(p.__dict__)  #{'_name': 'John'}
# print(p.name)    # John
#
# p.name = 'John Wick'
# print(p.__dict__)   #{'_name': 'John Wick'}
# print(p.name)    #John Wick
# del p.name
# print(p.__dict__)   # {}
# print(p.name)       # AttributeError:
###################





### 22. Property Decorators - Coding
#
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self,value):
#         self._name = value
#
#
# p = Person('Alex')
#
# print(p.name)  #Alex
#
# p.name = 'John'
# print(p.name)  #John
#
###################



### 24. Read-Only and Computed Properties - Coding
#
# from math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#         self._area = None
#
#     @property
#     def radius(self):
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):
#         self._area = None
#         self._radius = value
#
#     @property
#     def area(self):
#         if self._area is None:
#             print('Calculating area...')
#             self._area = pi * (self.radius ** 2)
#         return self._area
#
# c = Circle(1)
#
# print(c.area)     #Calculating area...   3.141592653589793
# print(c.area)     # 3.141592653589793
#
# c.radius = 2
#
# print(c.area)     #Calculating area...   12.566370614359172
# print(c.area)     # 12.566370614359172
#
##############################


### 26. Deleting Properties - Coding
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self,value):
#         self._name = value
#
#     @name.deleter
#     def name(self):
#         del self._name
#
#
# p = Person('Alex')
# print(p.__dict__)  #{'_name': 'Alex'}
# print(p.name)   #Alex
#
# del p.name
# print(p.__dict__)   #{}
#
#################
