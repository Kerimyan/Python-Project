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
# sorted(t, key=lambda s: len(s))  #will return the same thing as with |def sort_key(s): |  ill return sorted words in list (based on the length of strings)
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


#################################################################################################################################################################
#################################################################################################################################################################

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
# print(d, id(d))                #the result must be same but id not  ((   {'a': 123, 'b': [1, 2, 33, 4], 'c': {'aa': 222, 'bb': 333}} 140006329804928
# print(d_copy, id(d_copy))      #the result must be same but id not  ((   {'a': 123, 'b': [1, 2, 33, 4], 'c': {'aa': 222, 'bb': 333}} 140006329835968
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







#################################################################################################################################################
#################################################################################################################################################




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
