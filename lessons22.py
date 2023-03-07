# #, [27.02.23 23:32]
# # my_var = 10
# # print(my_var)
# # print(id(my_var))
# # print(hex(id(my_var)))
# # greeting="hello"
# # print(id(greeting))
# # print("This is a hex:" + hex(id(greeting)))
import copy
import numbers
import sys
import ctypes
import gc
import time
import math
from fractions import Fraction
from math import isclose
from math import trunc
from math import floor
from math import ceil
from math import copysign
from decimal import Decimal
import string
from dis import dis
from timeit import timeit
import random
from copy import deepcopy
from functools import lru_cache
from collections import namedtuple

#
# # a=[1,2,3]
# # print(id(a))
# # print(sys.getrefcount(a))
# # print(a)
# # def ref_count(address: int):
# #     return ctypes.c_long.from_address(address).value
# # ref_count(id(a))
# # print(ref_count(id(a)))
# # # b = a
# # # print(id(b))
# # # print(ref_count(id(a)))
# # b = a
# # id(b)
# # ref_count(id(a))
# # print(ref_count(id(a)))
# # c = 10
# # print(ref_count(id(a)))
# # b=None
# # print(ref_count(id(b)))
# # a_id =id(a)
# # a=None
# # ref_count(a_id)
# # print(ref_count(a_id))
# # print(ref_count(a_id))
#
# # a = "hello"
# # print(type(a))
# # a = 10
# # print(type(a))
#
# # a = lambda x: (x**2)+2
# # print(a(2))
# # a = 4+5j
# # print(a)
#
#
# # myvar = 10
# # myvar+=5
# # print(myvar)
#
# # a = 10
# # print(id(a))
# # print(type(a))
# # a = 15
# # print(id(a))
#
# # a = 10
# # b = 10
# # print(id(a))
# # print(id(b))
#
# # my_list = [1,2,3]
# # type(my_list)
# # print(type(my_list))
# # print(my_list)
# # print(id(my_list))
# # my_list.append(4)
# # print(my_list)
# # print(id(my_list))
# # my_list_1=[1,2,3]
# # print(id(my_list_1))
# # my_list_1 = my_list_1 + [4]
# # print(my_list_1)
# # my_dict = dict(key1=1,key2='a')
# # print(my_dict)
# # print(id(my_dict))
# # t = (1, 2, 3)
# # id(t)
# # print(t[0])
# # t1 = ([1,2], [3,4])
# # print(t1[1])
# # t1[0].append(3)
# # print(t1[0])
# # t1[1].append(5)
# # t1[1].append(6)
# # print(t1[1])
#
#
# # def process(s):
# #     print('Initial s # = {0}'.format(id(s)))
# #     s = s + " world"
# #     print('Final s # = {0}'.format(id(s)))
# # my_var = 'hello'
# # print('my_var # = {0}'.format(id(my_var)))
# # process(my_var)
# # print(id(my_var))
# # print(my_var)
# # def modify_list(lst):
# #     print('Initial lst # = {0} '.format(id(lst)))
# #     lst.append(100)
# #     print('Final lst # = {0} '.format(id(lst)))
# # my_list = [1,2,3]
# # print(id(my_list))
# # modify_list(my_list)
# # print(my_list)
# # def modify_tuple(t):
# #     print('Initiate t # = {0}'.format(id(t)))
# #     t[0].append(100)
# #     print('Initiate t # = {0}'.format(id(t)))
# # my_tuple = ([1,2], 'a')
# # id(my_tuple)
# # modify_tuple(my_tuple)
# # print(my_tuple)
#
# # a = "hello"
# #
# # b = a
# # print(hex(id(a)))
# # print(hex(id(b)))
# #
# # a = "heelo"
# # b = "hello"
# # print(hex(id(a)))
# # print(hex(id(b)))
# # b = "hello world"
# # print(hex(id(b)))
# # print(hex(id(a)))
# # print(a)
# # print(b)
# # a = [1,2,3]
# # b= a
# # print(hex(id(a)))
# # print(hex(id(b)))
# # b.append(100)
# # print(b)
# # print(id(b))
# # print(id(a))
# #
# #
# # a = 500
# # b = 500
# # print(id(a))
# # print(id(b))
#
# # a=10
# # b=10
# # print(id(a))
# # print(id(b))
# # print("a is b", a is b)
# # print("a==b", a==b)
#
# # a=900
# # b=900
# # print(sys.getrefcount(a),sys.getrefcount(b))
# # print(id(a))
# # print(id(b))
# # print("a is b ", a is b)
# # print("a ==b ", a==b)
# # a = [1,2,3]
# # b = [1,2,3]
# # print(id(a))
# # print(id(b))
# # print("a is b: ", a is b)
# # print("a == b: ", a == b)
# #
# # a=10
# # b=10.0
# # print(a is b)
# # print(a == b)
# # a = 10 + 0j
# #
# # type(a)
# # print(type(a))
# # print(type(b))
# # print("a is b: ", a is b)
# # print("a == b: ", a == b)
# #
# #
# # print(id(None))
# # # print(type(None))
# #
# # a= None
# # b=None
# # c=None
# # print(a is b)
# # print(a is c)
# # print(a == b)
# # print(a == b)
#
# # a = 10
# # print(type(a))
# # b = int(10)
# # print(type(b))
# # help(int)
# # print(help(int))
#
# # c = int()
# # # print(c)
# # c = int('A', base=2)

# #, [27.02.23 23:32]
# # print(c)
#
# # def square(a):
# #     return a**2
# # # print(type(square))
# # f = square
# # # print(id(square))
# # # print(id(f))
# # # print(f is square)
# # print(f(2))
# #
# # def cube(a):
# #     return a**3
# # def select_function(fn_id):
# #     if fn_id ==1:
# #         return square
# #     else:
# #         return cube
# # f=select_function(1)
# # # print(f is square)
# # # f = select_function(2)
# # # print(f is cube)
# # print(f(5))
#
# # a = [1,2,3]
# # print(id(a))
# # # print(sys.getrefcount(a))
# # def ref_count(address: int):
# #     return ctypes.c_long.from_address(address).value
# # print(ref_count(id(a)))
#
# # 2 Variables are Memory References
# # a = [1,2,3]
# # print(id(a))
# # print(sys.getrefcount(a))
# # def ref_count(address: int):
# #     return ctypes.c_long.from_address(address).value
# # print(ref_count(id(a)))
# # b=a
# # c=10
# # b=None
# # a_id=id(a)
# # a=None
# # print(ref_count(id(a)))
#
# # 4 garbage collection
# # def ref_count(address):
# #     return ctypes.c_long.from_address(address).value
# # def object_by_id(object_id):
# #     for obj in gc.get_objects():
# #         if id(obj) == object_id:
# #             return "Object exists"
# #     return "Not found"
# # class A:
# #     def init(self):
# #         self.b = B(self)
# #         print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))
# # class B:
# #     def init(self, a):
# #         self.a = a
# #         print('B: self: {0}, A: {1}'.format(hex(id(self)),hex(id(self.a))))
# # gc.disable()
# # my_var = A()
# # print(hex(id(my_var)))
# # print(hex(id(my_var.b)))
# # print(hex(id(my_var.b.a)))
# # a_id=id(my_var)
# # b_id=id(my_var.b)
# # print(hex(a_id),hex(b_id))
# # print(ref_count(a_id))
# # print(ref_count(b_id))
# # print(object_by_id(a_id))
# # print(object_by_id(b_id))
# # my_var=None
# # print(ref_count(a_id))
# # print(ref_count(b_id))
# # print(gc.collect())
# # print(object_by_id(a_id))
# # print(object_by_id(b_id))
# # print(ref_count((a_id)))
# # print(ref_count((b_id)))
#
# # 5 dynamic vs static typing
# # a = "hello"
# # print(type(a))
# # a = 10
# # print(type(a))
# # a=lambda x: x**2
# # print(a(2))
# # print(type(a))
# # a=3+4j
# # print(type(a))
#
#
# # 6 Variable Re-Assignment
# # a = 10
# # print(hex(id(a)))
# # print(type(a))
# # a = 15
# # print(hex(id(a)))
# # a = a + 1
# # print(hex(id(a)))
# # a=10
# # b=10
# # print(hex(id(a)),hex(id(b)))
#
# # 7 Object Mutability
# # my_list = [1,2,3]
# # print(type(my_list))
# # print(id(my_list))
# # my_list.append(4)
# # print(my_list)
# # print(id(my_list))
# # my_list_1=[1,2,3]
# # print(id(my_list_1))
# # print(my_list_1)
# # my_list_1+=[4]
# # print(my_list_1)
# # print(id(my_list_1))
# # my_dict = dict(key1=1, key2='a')
# # print(my_dict)
# # print(id(my_dict))
# # my_dict['key3'] = 12.5
# # print(my_dict)
# # print(my_dict['key3'])
# # print(type(my_dict))
# # print(id(my_dict))
# # t = (1,2,3)
# # print(id(t))
# # print(t[0],t[1],t[2])
# # t = ([1,2], [3,4])
# # print(id(t))
# # t[0].append(3)
# # print(t)
#
# # 8 Function Arguments and Mutability
# # def process(s):
# #     print('Initial s # = {0}'.format(id(s)))
# #     s = s + ' world'
# #     print('Final s # = {0}'.format(id(s)))
# # my_var = 'hello'
# # print('my_var # = {0}'.format(id(my_var)))
# # print(process(my_var))
# # print(id(my_var))
# # print(my_var)
# # def modify_list(lst):
# #     print('Initial s # = {0}'.format(id(lst)))
# #     lst.append(100)
# #     print('Final s # = {0}'.format(id(lst)))
# # my_list = [1,2,3]
# # print(id(my_list))
# # print(modify_list(my_list))
# # print(id(my_var))
# # print(my_list)
# # def modify_tuple(t):
# #     print('Initial s # = {0}'.format(id(t)))
# #     t[0].append(100)
# #     print('Final s # = {0}'.format(id(t)))
# # my_tuple=([1,2], 'a')
# # print(id(my_tuple))
# # print(modify_tuple(my_tuple))
# # print(my_tuple)
#
# # 9 Shared References and Mutability
# # a="hello"
# # b=a
# # print(hex(id(a)))
# # print(hex(id(b)))
# # a="hello"
# # b="hello"
# # print(hex(id(a)),hex(id(b)))
# # b = "hello world"

# #, [27.02.23 23:32]
# # print(hex(id(a)),hex(id(b)))
# # a = [1,2,3]
# # b = a
# # print(hex(id(a)),hex(id(b)))
# # """mem address"""
# # b.append(100)
# # print(a,b)
# #
# # a =10
# # b = 10
# # print(id(a),id(b))
# # a = 500
# # b = 500
# # print(id(a),id(b))
#
# # 10 Variable Equality
# # x = 10
# # print(x is not None)
# # a=10
# # b=10
# # print(id(a))
# # print(id(b))
# # print("a is b",a is b)
# # print("a == b",a == b)
# # a= 500
# # b =500
# # print(id(a),id(b))
# # print("a is b", a is b)
# # a =[1,2,3]
# # b =[1,2,3]
# # print("a is b", a is b)
# # print("a == b", a == b)
# # a = 10 + 0j
# # print(type(a))
# # print(id(None))
# # a=None
# # b=None
# # c=None
# # print(a is b)
# # print(a is c)
#
# # 11 Everything is an Object
# # a = 10
# # print(type(a))
# # b=int(10)
# # print(type(b))
# # print(b)
# # help(int)
# # c = int()
# # print(c)
# # c =int('1010',base=2)
# # print(c)
#
# # def square(a):
# #     return a**2
# # # print(type(square))
# # # f = square
# # print(id(square))
# # # print(f is square)
# # # print(square(2))
# # def cube(b):
# #     b**3
# # def select_function(fn_id):
# #     if fn_id == 1:
# #         return square
# #     else:
# #         return cube
# # f = select_function(3)
# # # print(f is square)
# # print(f(4))
# #
# # def square(a):
# #     return a**2
# # def cube(b):
# #     return b**3
# # def my_func(func_id):
# #     if func_id==None:
# #         return square
# #     else:
# #         return cube
# # f = my_func(2)
# # # print(my_func(None)(3))
# # print(my_func(2)(3))
# # # print(None == False)
# # # print(type(...))
# # # help(None)
# #
# # def exec_function(fn, n):
# #     return fn(n)
# # exec_function(cube, 3)
# # exec_function(square,4)
# # print(exec_function(square,2))
# # print(exec_function(cube,4))
#
# # 12 Python Optimizations Interning
# # [-5,256]
# # a = 10
# # b = 10
# # print(id(a),id(b))
# # c=-5
# # d=-5
# # print(id(c),id(d))
# # print(a is b)
# # print(a==b)
# # a=257
# # b=257
# # print(a is b)
# # a = 10
# # b = int(10)
# # c = int('10')
# # d = int('1010',2)
# # print(a,b,c,d)
# # print(id(a),id(b),id(c),id(d))
#
# # 13 Python Optimizations String Interning
# # a = 'hello'
# # b = 'hello'
# # print(a is b, a == b)
# # print(id(a),id(b))
# # a = 'hello world'
# # b = 'hello world'
# # print(id(a),id(b))
# # print(a==b)
# # print(a is b)
# # a = '_this_is_a_long_string'
# # b = '_this_is_a_long_string'
# # print(id(a),id(b))
# # print(a is b)
# # a = sys.intern('hello world')
# # b = sys.intern('hello world')
# # c = 'hello world'
# # # tarbervum e aic ev bic c-n
# # print(id(a), id(b), id(c))
# # print(a==b)
# # print(a is b,)
# # def compare_using_equals(n):
# #     a = 'a long string that is not interned' * 200
# #     b = 'a long string that is not interned' * 200
# #     for i in range(n):
# #         if a == b:
# #             pass
# #
# #
# # def compare_using_interning(n):
# #     a = sys.intern('a long string that is not interned' * 200)
# #     b = sys.intern('a long string that is not interned' * 200)
# #     for i in range(n):
# #         if a is b:
# #             pass
# #
# #
# # import time
# #
# # start = time.perf_counter()
# # compare_using_equals(10000000)
# # end = time.perf_counter()
# # print('equality', end - start)
# #
# # start = time.perf_counter()
# # compare_using_interning(10000000)
# # end = time.perf_counter()
# # print('equality', end - start)
#
# # 14 Python Optimizations Peephole
# # def my_func():
# #     a = 24 * 60
# #     1440
# #     b = (1,2) * 5
# #     tpeluya senc (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
# #     c = 'abc' * 3
# #     'abcabcabc'
# #     d = 'ab' * 11
# #     'ab', 11,
# #     'ababababababababababab'
# #     e = 'the quick brown fox ' * 2
# #     'the quick brown fox the quick brown fox '
# #     f = ['a','b'] * 3
# #     ('a', 'b', 3)
# # print(my_func.code.co_consts)
# # def my_func(e):
# #     if e in [1,2,3]:
# #         pass
# # print(my_func.code.co_consts)
# # def my_func(e):
# #     if e in {1,2,3}:
# #         pass
# # print(my_func.code.co_consts)
# # import string
# # import time
# #, [27.02.23 23:32]
# # print(string.ascii_letters)
# # char_list = list(string.ascii_letters)
# # char_tuple = tuple(string.ascii_letters)
# # char_set = set(string.ascii_letters)
# # print(char_list,char_tuple,char_set)
# #
# # def membership_test(n, container):
# #     for i in range(n):
# #         if 'z' in container:
# #            pass
# # start = time.perf_counter()
# # membership_test(10000000,char_list)
# # end = time.perf_counter()
# # print('list: ',end-start)
# # start = time.perf_counter()
# # membership_test(10000000,char_tuple)
# # end = time.perf_counter()
# # print('tuple: ', end-start)
# # start = time.perf_counter()
# # membership_test(10000000,char_set)
# # end = time.perf_counter()
# # print('set: ',end-start)
#
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
# # 6. Booleans Boolean Operators - Lecture
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
#
# # 2. Sequence Types - Lecture
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
# # 3. Sequence Types - Coding.
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
#
# # 9. Copying Sequences - Coding.
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
#
# # 10. Slicing - Lecture.
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
#
# # 11. Slicing - Coding.
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
#
# # 12. Custom Sequences - Part 1 - Lecture
# # my_list = ['a','b','c','d','e','f']
# # print(my_list.getitem(0))
# # print(my_list.getitem(1))
# # print(my_list.getitem(2))
# # print(my_list.getitem(-2))
# # print(my_list.getitem(slice(None,None,-1)))
# # print(my_list.getitem(100))
# # print(my_list.getitem(-100))
#
# # my_list = [0,1,2,3,4,5]

# #, [27.02.23 23:32]
# # for item in my_list:
# #     print(item 2 )
# # print(len(my_list))
# # print(my_list.__len__())
#
# # 13. Custom Sequences - Part 1 - Coding
# # my_list = [1, 2, 3, 4, 5]
# # print(len(my_list))
# # print(my_list.__len__())
# # print(my_list[3])
# # print(my_list.__getitem__(2))
# # print(my_list[::-1])
# # print(my_list.__getitem__(slice(None, None, -1)))
# # for item in my_list:
# #     print(item  2)
# # print()
#
# # my_list = [1, 2, 3, 4, 5]
# # index = 0
# # while True:
# #     try:
# #         item = my_list.getitem(index)
# #     except IndexError:
# #         break
# #     print(item  2)
# #     index += 1
#
# # print(my_list.__getitem__(index))
# # index +=1
# # print(my_list.__getitem__(index))
# # index +=1
# # print(my_list.__getitem__(index))
#
# # class Silly:
# #     def __init__(self, n):
# #         self.n = n
# #
# #     def __len__(self):
# #         print('Called __len')
# #         return self.n
# #     def __getitem__(self, value):
# #         print(type(value))
# #         print(f'You requested item at {value}')
# # if value <0 or value >=self.n:
# #     raise IndexError
# # else:
# # return 'This is a silly element'
# # silly = Silly(3)
# # print(silly[0:5:2])
# # print(len(silly))
# # print(silly.__getitem__(1000))
# # print(silly.__getitem__(1020))
#
# #
# # for item in silly:
# #     print(item*2)
#
# # @lru_cache(2**10)
# # def fib(n):
# #     if n < 2:
# #         return 1
# #     else:
# #         return fib(n-1) + fib(n-2)
# # # print(fib(7))
# # print(fib(5))
#
# # class Fib:
# #     def __init__(self, n):
# #         self.n = n
# #
# #     def __len__(self):
# #         return self.n
# #
# #     def __getitem__(self, s):
# #         if isinstance(s, int):
# #             if s < 0 or s >= self.n:
# #                 raise IndexError
# #             else:
# #                 return Fib._fib(s)
# #     @staticmethod
# #     @lru_cache(2 * 10)
# #     def _fib(n):
# #         if n < 2:
# #             return 1
# #         else:
# #             return Fib._fib(n-1) + Fib._fib(n-2)
# # f = Fib(10)
# # print(list(f))
# # print(f[6])
# # print([item  2 for item in f])
# # for item in f:

# #, [27.02.23 23:32]
# #     print(item  2)
#
#
# # class Fib:
# #     def __init__(self, n):
# #         self.n = n
# #
# #     def __len__(self):
# #         return self.n
# #
# #     def __getitem__(self, s):
# #         if isinstance(s, int):
# #             if s < 0:
# #                 s = self.n + s
# #             if s < 0 or s >= self.n:
# #                 raise IndexError
# #             else:
# #                 return Fib._fib(s)
# #     @staticmethod
# #     @lru_cache(2 * 10)
# #     def _fib(n):
# #         if n < 2:
# #             return 1
# #         else:
# #             return Fib._fib(n-1) + Fib._fib(n-2)
#
#
# # fib = Fib(10)
# # print(list(fib))
# # print(fib[5])
# # print(fib[9])
# # result = fib[0:5]
# # print(type(result))
# # result = fib.__getitem__(slice(0,5))
# # print(result)
#
#
# # class Fib:
# #     def __init__(self, n):
# #         self.n = n
# #
# #     def __len__(self):
# #         return self.n
# #
# #     def __getitem__(self, s):
# #         if isinstance(s, int):
# #             if s < 0:
# #                 s = self.n + s
# #             if s < 0 or s >= self.n:
# #                 raise IndexError
# #             else:
# #                 return Fib._fib(s)
# #         else:
# #             # range_tuple = s.indices(self.n)
# #             start,stop,step = s.indices(self.n)
# #             rng = range(start,stop,step)
# #             # print(range_tuple)
# #             return [Fib._fib(i) for i in rng]
# #     @staticmethod
# #     @lru_cache(2 * 10)
# #     def _fib(n):
# #         if n < 2:
# #             return 1
# #         else:
# #             return Fib._fib(n-1) + Fib._fib(n-2)
# #
# # fib = Fib(10)
# # print(fib[0:4])
# # print(fib[-1:-4:-1])
# # print(list(range(9,6,-1)))
#
# # 14. In-Place Concatenation and Repetition - Lecture.
# # l1 = [1,2,3]
# # l2 = [4,5,6]
# # l1+=l2
# # print(l1,l2)
# # l1 = l1 * 2
# # l1*=2
# # print(l1)
#
# # 15. In-Place Concatenation and Repetition - Coding.
# # l1 = [1,2,3,4]
# # l2 = [5,6]
# # print(id(l1),(l1))
# # print(id(l2),(l2))
# # l1 = l1 + l2
# # print(id(l1),l1)
#
# # t1 = (1,2,3)
# # l1 = l1 + t1
# # print(l1)
#
#
# # l1 = [1,2,3,4]
# # l2 = [5,6]
# # print(id(l1),(l1))
# # print(id(l2),(l2))
# # l1 +=l2
# # print(id(l1),l1)
#
# # l1 = [1, 2, 3, 4]
# # t1 = (5, 6)
# # l1 += t1
# # print(id(l1), l1)
# # print(id(t1), t1)
# # l1 += range(7, 11)
# # print(id(l1), l1)
# # l1 += [100, 'X', 'a']
# # print(id(l1), l1)
# # t1 = (1, 2, 3)
# # t2 = (4, 5, 6)
# # print(id(t1), t1)
# # print(id(t2), t2)
# # t1 += t2
# # print(id(t1), t1)
# # l1 = [1,2,3]
# # l1 = l1 * 2
# # print(l1)
# # t1 = (1,2,3)
# # t1 = t1 * 2
# # print(t1)
#
# # 16. Assignments in Mutable Sequences - Lecture.
# # l = [1, 2, 3, 4, 5]
# # l[1:3] = (10, 20, 30)
# # print(l)
# # print(l[0:4:2])
# # l[0:4:2] = [10, 30]
# # print(l)
#
# # l = [1,2,3,4,5]
# # l[2:3] = []
# # l[1:1] = 'abc'
# # print(l)
#
# # 17. Assignments in Mutable Sequences - Coding.
# # l = [1,2,3,4,5]
# # print(id(l))
# # print(l[0:3])
# # l[0:3]= 'python'
# # print(l)
# # print(l[2:5])
# # l[2:5] = []
# # print(l)
# # l[2:5] =''
# # print(l)
# # print(len(''))
# # l = [1,2,3,4,5]
# # print(l[2:2])
# # s = slice(2,2)
# # print(l[s])
# # print(s.start,s.stop)
# # l[2:2] = ('a',100,500)
# # print(l)
# # t = (1,2,3,4,5)
# # print(t[0:3])
#
# # l = [1,2,3,4,5]
# # l[0:5:2]
# # l[0:5:2] = 'abc'
# # print(l)
#
# # 18. Custom Sequences - Part 2 - Lecture.
#
# # a = 2
# # b = 4
# # c = a.__add__(b)
# # d = a.__mul__(b)
# # e = a.__radd__(b)
# # f = a.__rmul__(b)
# #
# # print(c,d,e,f)
#
# # 19. Custom Sequences - Part 2A - Coding.
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
# def __repr__(self):
#     return f'MyClass(name={self.name})'
#
# def __add__(self, other):
#     print(f'You called + on {self} and {other}')
#     return 'Hello from __add__'
#
# def __iadd__(self, other):
#     print(f'You called += on {self} and {other}')
#     return 'Hello from __iadd'
#
#
# c1 = MyClass('istance 1')
# c2 = MyClass('istance 2')
#
# result = c1 + c2
# print(result)
# print(c1,c2)
# c1+=c2
# prin

# #, [27.02.23 23:32]
#t(c1,c2)
#
# # class MyClass:
# #     def __init__(self, name):
# #         self.name = name
#
# # def __repr__(self):
# #     return f'MyClass(name={self.name})'
#
# # def __add__(self, other):
# #     return MyClass(self.name + other.name)
#
# # def __iadd__(self, other):
# #     if isinstance(other,MyClass):
# #         self.name += other.name
# #     else:
# #         self.name += other
# #     return self
#
#
# # c1 = MyClass('Eric')
# # c2 = MyClass('Idle')
# # print(c1,c2)
# # result = c1+c2
# # print(result)
# # c1+=c2
# # print(c1)
#
# # class MyClass:
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def __repr__(self):
# #         return f'MyClass(name={self.name})'
# #
# #     def __add__(self, other):
# #         return MyClass(self.name + other.name)
# #
# #     def __iadd__(self, other):
# #         if isinstance(other,MyClass):
# #             self.name += other.name
# #         else:
# #             self.name += other
# #         return self
# #     def __mul__(self, n):
# #         return MyClass(self.name * n)
# #     def __imul__(self, n):
# #         self.name *= n
# #         return self
# # c1 = MyClass('Eric')
# # print(c1)
# # result = c1 * 3
# # print(result)
# # c1*=3
# # print(c1)
# # c1 = MyClass('Eric')
# # c1 = 3
# # print(c1)
# # print((3).__mul__(c1))
# # print(c1.__rmul__(3))
# # print(3 * c1)
#
#
# # class MyClass:
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def __repr__(self):
# #         return f'MyClass(name={self.name})'
# #
# #     def __add__(self, other):
# #         return MyClass(self.name + other.name)
# #
# #     def __iadd__(self, other):
# #         if isinstance(other, MyClass):
# #             self.name += other.name
# #         else:
# #             self.name += other
# #         return self
# #
# #     def __mul__(self, n):
# #         return MyClass(self.name * n)
# #
# #     def __rmul__(self, n):
# #         return self.__mul__(n)
# #
# #     def __imul__(self, n):
# #         self.name *= n
# #         return self
#
#
# # c1 = MyClass('Eric')
# # print(c1 * 3)
# # print(3 * c1)
#
#
# # class MyClass:
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def __repr__(self):
# #         return f'MyClass(name={self.name})'
# #
# #     def __add__(self, other):
# #         return MyClass(self.name + other.name)
# #
# #     def __iadd__(self, other):
# #         if isinstance(other, MyClass):
# #             self.name += other.name
# #         else:
# #             self.name += other
# #         return self
# #
# #     def __mul__(self, n):
# #         return MyClass(self.name * n)
# #
# #     def __rmul__(self, n):
# #         return self.__mul__(n)
# #
# #     def __imul__(self, n):
# #         self.name *= n
# #         return self
# #
# #     def __contains__(self, value):
# #         return value in self.name
# #
# #
# # c1 = MyClass('Eric Idle')
# # print('Eric' in c1)
# # print('I' in c1)
# # print('i' in c1)
# # print('p' in c1)
#
# # 20. Custom Sequences - Part 2B - Coding.
# # Point = namedtuple('Point', 'x y')
# # p1 = Point(10.5,3.2)
# # print(p1)
# # p1 = Point('abc', [1,2,3])
# # print(p1)
# # x,y = p1
# # print(x)
# # print(y)
# #
# # print(isinstance(10,numbers.Number))
# # print(isinstance(10.5,numbers.Number))
# # print(isinstance(10+2j,numbers.Number))
# # print(isinstance(10+2j,numbers.Real))
# # print(isinstance(10,numbers.Real))
#
# class Point:
#     def __init__(self, x, y):
#         if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
#             self._pt = (x, y)
#         else:
#             raise TypeError('Point co-ordinates must be real numers.')
#
#     def __repr__(self):
#         return f'Point(x={self._pt[0]}, y={self._pt[1]})'
#
#
# # p1 = Point(10, 2.5)
# # print(p1)
# # p1 = Point('abc',10)
#
# class Point:
#     def __init__(self, x, y):
#         if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
#             self._pt = (x, y)
#         else:
#             raise TypeError('Point co-ordinates must be real numers.')
#

# #, [27.02.23 23:32]
#     def __repr__(self):
#         return f'Point(x={self._pt[0]}, y={self._pt[1]})'
#
#     def __len__(self):
#         return len(self._pt)
#
#     def __getitem__(self, s):
#         return self._pt[s]
#
#
# #
# #
# # p1 = Point(10, 2)
#
#
# # x,y = p1
# # print(p1)
# # print(x)
# # print(y)
# # p2 = Point(*p1)
# # print(p1)
# # print(id(p1),id(p2))
# class Polygon:
#     def __init__(self, *pts):
#         if pts:
#             self._pts = [Point(*pt) for pt in pts]
#         else:
#             self._pts = []
#
#     def __repr__(self):
#         pts_str = ', '.join([str(pt) for pt in self._pts])
#         return f'Polygon({self._pts})'
#
#
# #
# #
# # # p = Polygon((0, 0), Point(1, 1))
# # # print(p)
# #
# #
# class Polygon:
#     def __init__(self, *pts):
#         if pts:
#             self._pts = [Point(*pt) for pt in pts]
#         else:
#             self._pts = []
#
#     def __repr__(self):
#         pts_str = ', '.join([str(pt) for pt in self._pts])
#         return f'Polygon({pts_str})'
#
#     def __len__(self):
#         return len(self._pts)
#
#     def __getitem__(self, s):
#         return self._pts[s]
#
#     def __setitem__(self, s, other):
#         self._pts[s] = [Point(*pt) for pt in value]
#
#     def __add__(self, other):
#         if isinstance(other, Polygon):
#             new_pts = self._pts + other._pts
#             return Polygon(*new_pts)
#         else:
#             raise TypeError('can only concatenate with another Polygon')
#
#
# def __iadd__(self, other):
#     if isinstance(other, Polygon):
#         self._pts = self._pts + other._pts
#         return self
#     else:
#         points = [Point(*pt) for pt in other]
#     self._pts = self._pts + points
#     return self
#
#     def append(self, pt):
#         self._pts.append(Point(*pt))
#
#     def insert(self, i, pt):
#         self._pts.insert(i, Point(*pt))
#
#     def extend(self, pts):
#         if isinstance(pts, Polygon):
#             self._pts += pts._pts
#         else:
#             points = [Point(*pt) for pt in pts]
#             self._pts += points
#
#     def __iadd__(self, other):
#         self.extend(other)
#         return self
#
#
# #
# # p1 = Polygon((0,0),(1,1))
# # p2 = Polygon((2,2),(3,3))
# # print(p1)
# # print(p2)
# # p1.append([10,10])
# # print(p1)
# # p1.insert(1,Point(-1,-1))
# # print(p1)
# # p1.extend(p2)
# # print(p1)
# # p1.extend([(0,0),Point(20,20)])
# # print(p1)
#
# # p1 = Polygon((0, 0), (1, 1))
# # p2 = Polygon((2, 2), (3, 3))
# # print(p1+p2)
#
# # p = Polygon((0, 0), Point(1, 1))
# # p1 = Polygon(Point(x=0, y=0), Point(x=1, y=1))
# # print(p)
# # print(p1)
# # print(p[0])
# # print(p[0:2])
# # print(p[::-1])
# # p1 += p2
# # print(p1)
# # p1 = p1.__iadd__(p2)
# # print(p1)
# # p1 += [(2, 2), (3, 3), Point(4, 4)]
# # print(p1)
#
# # 21. Custom Sequences - Part 2C - Coding.
# 23. Sorting Sequences - Coding.mp4
# t = 10, 3, 5, 6, 8, 9, 4, 1
# print(sorted(t))
# t = 1+1j,10,20,40
# print(sorted(t))
# s = {10,2,5,8,3,1,0}
# print(sorted(s))
# d = {3: 100, 2: 200, 1: 10}
# print(sorted(d))
# d1 = {'b': 100, 'a': 50, 'c': 80}
# print(sorted(d1))
# print(sorted(d1, key=lambda k: d1[k]))
# print(d1['a'])
# print(d1['b'])
# print(d1['c'])
# t = 'this', 'parrot', 'is', 'a', 'late', 'bird'
# print(sorted(t))


# def sorted_key(s):
#     return len(s)
#
#
# print(sorted(t, key=lambda s: len(s)))

# t = 'aaaa','bbbb', 'e'*4, 'dddd','c'*4
# print(t)
# print(sorted(t))
# print(sorted(t, key=lambda t: len(t)))
# print(abs(1+1j))
# t = 0, 10+10j,3-3j,4+4j,5-2j
# print(sorted(t,key=abs))
# print(sorted(t,key=lambda t: t.imag))
# print(sorted(t,key=lambda t: t.imag, reverse=True))

# t = 'this', 'parrot', 'is', 'a', 'late', 'bird'
# print(sorted(t, reverse=True))
# print(sorted(t, key=lambda s: len(s), reverse=True))
# print(sorted(t, key=lambda s: -len(s), reverse=True))

# #, [27.02.23 23:32]
# l = ['this', 'bird', 'is', 'a', 'late', 'parrot']
# l = 'this bird is a late parrot'.split(' ')
# print(l)
# print(sorted(l, key=lambda s: len(s)))
# print(l)
# result = (l.sort(key=lambda s: len(s)))
# print(result)
# print(type(result))
# print(l)
# #
# random.seed(0)
# n = 10_000_000
# l = [random.randint(0, 100) for n in range(n)]
# print(l[0:10])
# print(timeit(stmt='sorted(l)', globals=globals(), number=1))
# print(l[0:10])
# print(timeit(stmt='l.sort()', globals=globals(), number=1))
# print(l[6_000_000:6_000_010])

# 24. List Comprehensions - Lecture.
# other_list = ['this', 'is', 'a', 'parrot']
# new_list = []
# for item in other_list:
#     if len(item) > 2:
#         new_list.append(item[::-1])
# print(new_list)


# sq = [i**2 for i in range(1,12) if i%2 and i%3 and i%5]
# print(sq)

# def temp():
#     new_list = []
#     for i in range(10):
#         new_list.append(i**2)
#     return new_list
# print(temp())

# num = 10
# sq = [item**2 for item in range(num)]
# print(sq)

# sq = [item  2 for item in range(10)]
# print(sq)

# def my_func(num):
#     sq = [item 2 for item in range(num)]
#     return sq
# print(my_func(12))

# l = []
# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             l.append((i,j,k))
# print(l)

# l = []
# for i in range(5):
#     for j in range(5):
#         if i==j:
#             l.append((i,j))
# print(l)

# l = []
# for i in range(1,6):
#     if i%2 ==0:
#         for j in range(1,6):
#             if j%3==0:
#                 l.append((i,j))
# print(l)
# [(i,j)
# for i in range(1,6) if i%2==0
# for i in range(1,6) if i%3==0]

# l = []
# for i in range(1,6):
#     for j in range(1,6):
#         if i%2==0:
#             if j%3==0:
#                 l.append((i,j))
# print(l)

# 25. List Comprehensions - Coding.
# squares = []
# for i in range(1, 101):
#     squares.append(i  2)
# print(squares[0:11])

# squares = [i  2 for i in range(1, 101)]
# print(squares[0:10])

# squares = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         squares.append(i  2)
# print(squares[0:10])

# squares = [i  2 for i in range(1, 10) if i % 2 == 0]
# print(squares[0:10])

# squares = [i  2
#            for i in range(1, 101)
#            if i % 2 == 0]
# print(squares[0:10])

# compiled_code = compile('[i**2 for i in (1,2,3)]',
#                         filename='string', mode='eval')
# print(compiled_code)
# import dis
# print(dis.dis(compiled_code))


# table = []
# for i in range(1,11):
#     row = []
#     for j in range(1,11):
#         row.append(i*j)
#     table.append(row)
# print(table)


# table2 = [
#     [i*j for j in range(1,11)]
#     for i in range(1,11)
# ]
# print(table2)


from math import factorial

# def combo(n, k):
#     return factorial(n) // (factorial(k) * factorial(n - k))
# print(combo(5,3))
# size = 10
# pascal = [[combo(n, k) for k in range(n + 1)] for n in range(size + 1)]
# print(pascal,'\t')

# l1 = ['a', 'b', 'c']
# l2 = ['x', 'y', 'z']
# result = []
# for s1 in l1:
#     for s2 in l2:
#         result.append(s1 + s2)
# print(result)

# result = [s1 + s2
#           for s2 in l2
#           for s1 in l1
#           ]
# print(result)

# l1 = ['a', 'b', 'c']
# l2 = ['b', 'c', 'd']
# result = []
# for s1 in l1:
#     for s2 in l2:
#         if s1 != l2:
#             result.append(s1 + s2)
# print(result)
# result = [s1 + s2 for s1 in l1 for s2 in l2 if s1 != s2]
# print(result)

# result = [s1 + s2 for s1 in l1 if s1 != 'a' for s2 in l2 if s1 != s2]
# print(result)

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = ['a', 'b', 'c', 'd', 'e']
# print(list(l1),list(l2))
# print(list(zip(l1,l2)))
#
# print(list(enumerate(l1)))
# print(list(enumerate(l2)))

# #, [27.02.23 23:32]
# result = []
# for index_1, item_1 in enumerate(l1):
#     for index_2, item_2 in enumerate(l2):
#         if index_1 == index_2:
#             result.append((item_1, item_2))
# print(result)
#
# result = [(item_1, item_2)
#           for index_1, item_1 in enumerate(l1)
#           for index_2, item_2 in enumerate(l2)
#           if index_1 == index_2]
# print(result)
#
# print(list(zip(l1, l2)))
#
# l = [1, 2, 3]
# print(sum(l))
#
# v1 = (1, 2, 3, 4, 5, 6)
# v2 = (10, 20, 30, 40, 50, 60)
# dot = 0
# for i in range(len(v1)):
#     dot += (v1[i] * v2[i])
# print(dot)
#
# print(list(zip(v1, v2)))
#
# print(sum([i * j for i, j in zip(v1, v2)]))

# l =[]
# for number in range(5):
#     l.append(number**2)
# print(l)
#
# # if 'number' in gloabals():
# #     del number
# l = [number**2 for number in range(5)]
# print(l)

# print('number' in globals())

# number = 100
# l = []
# for number in range(5):
#     l.append(number**2)
# print(l)
# print(number)


# l = [3,5,-1,0,9,67]
# i=0
# j=0
# for i in range(len(l)-1):
#     for j in range(len(l)-1):
#         if l[j] >= l[j+1]:
#             l[j] = l[j] + l[j+1]
#             l[j+1] = l[j] - l[j+1]
#             l[j] = l[j] - l[j+1]
# k = l
# print(k)

# 3. Creating Dictionaries - Coding

# a = {'k1': 100,'k2':200}
# print(type(a))
# print(a)
# a = (1, 2, 3)
# print(hash(a))
# d = {(1, 2, 3): 'This is a tuple'}
# print(d)
#
# t1 = (1, 2, 3)
# t2 = (1, 2, 3)
# print(t1 == t2)
# print(hash(t1) == hash(t2))
# print(id(t1), id(t2))
# print(d[t1])
# print(d[t2])
#
#
# def my_func(a, b, c):
#     print(a, b, c)
#
#
# print(hash(my_func))
#
# d = {my_func: [10, 20, 30]}
# print(d)
#
#
# def fn_Add(a, b):
#     return a + b
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
# funcs = {fn_Add: (10, 20), fn_inv: (7,), fn_mult: (2, 8)}
# print(funcs)
# for f in funcs:
#     res = f(*funcs[f])
#     print(res)
#
# # for f in funcs:
# #     result = f(*funcs[f])
# #     print(result)
#
# for f, args in funcs.items():
#     print(f, args)
# for f, args in funcs.items():
#     print(f(*args))
#
# d = dict(x=100, a=200)
# print(d)
# d = dict([('a', 100), ['x', 200]])
# print(d)
# d = {'a': 100, 'b': 200}
# print(d)
# d1 = dict(d)
# print(d1)
# d = {'a': 100, 'b': {'x': 1, 'y': 2}, 'c': [1, 2, 3]}
# print(d)
# d1 = dict(d)
# print(d1)
# print(id(d), id(d1))
# print(d is d1)
# d1['b'] = 1000
# print(d1)
# d1 = dict(d)
# print(d is d1)
# print(d['b'] is d1['b'])
# d1['b']['z'] = 100
# print(d1)
# d1['c'].append(4)
# print(d1)
#
# keys = ['a', 'b', 'c']
# values = (1, 2, 3)
# d = {}
# for k,v in zip(keys,values):
#     d[k] = v
# print(d)
#
#
# d = {k: v for k,v in zip (keys,values)}
# print(d)
#
#
#
#
# keys = 'abcd'
# values = range(1,5)
# d = {k:v for k,v in zip(keys,values)}
# print(d)
# d = {k:v for k,v in zip(keys,values) if v%2==0}
# print(d)


# x_coords = (-2,-1,0,1,2)
# y_coords = (-2,-1,0,1,2)
# gird = [(x, y)
#         for x in x_coords
#         for y in y_coords]

# print(gird)
# print(math.hypot(2, 2))

# gird_extended = [(x, y, math.hypot(x, y)) for x, y in gird]
# print(gird_extended)
# gird_extend = {(x,y): math.hypot(x,y) for x,y in gird}
# print(gird_extend)
# counters = dict.fromkeys(['a','b','c'],0)
# print(counters)
# counters = dict.fromkeys('abc',0)
# print(counters)
# d = dict.fromkeys('python')
# print(d)
# for k in d:
#     print(k)

# 4. Common Operations - Lecture

# 5. Common Operations - Coding
# d = dict(zip('abc', range(1, 4)))
# print(d)
# print(len(d))
# print(d['a'])
# print(d.get('a'))
# result = d.get('python')
# print(type(result))
# print(d.get('z','N/A'))
# print(d.get('a','N/A'))
# text = 'Se  tr grgofknfvoidsnvdf vdsfv dsovdsvndsv dsfvd svd sfvdsv dsfv dsf v dfv fd v sd vsd vf sd v sdv d vfvdfvdfv'
# counts= dict()
# for c in text:
#     counts[c] = counts.get(c, 0) + 1
# print(counts)











