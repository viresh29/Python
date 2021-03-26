import heapq
import re
from json import JSONEncoder
import json
import pysftp
from collections import Counter
import html
from inspect import signature
from functools import wraps
import os.path
import os
from functools import partial, wraps
from operator import attrgetter
from operator import itemgetter
from itertools import groupby
from collections import defaultdict
from itertools import compress
from collections import namedtuple
from collections import ChainMap  # logically merge dictionaries
import logging
import time
from random import randint

from abc import ABCMeta, abstractmethod
import io

avg = 123

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5448 N CLARK', 'date': '07/04/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'}
]

# sort by the desired field first
rows.sort(key=itemgetter('date'))

# Iterate in Groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('   ', i)


def timefunc(func):
    """ timefunc's doc """

    @wraps(func)
    def time_closure(*args, **kwargs):
        """ time_wrapper's doc string """
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Function: {func.__name__}, Time: {time_elapsed}")
        return result
    return time_closure


@timefunc
def single_thread(inputs):
    """
    Compute single threaded.
    """
    return [f(x) for x in inputs]


if __name__ == '__main__':

    demo_inputs = [randint(1, 100) for _ in range(10_000)]
    single_thread(demo_inputs)


class User:

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]

for u in users:
    print(u.user_id)


print(sorted(users, key=lambda u: u.user_id))
print(sorted(users, key=attrgetter('user_id')))

print(min(users, key=lambda u: u.user_id))
print(max(users, key=attrgetter('user_id')))


prices = {
    'ACME': 45.23,
    'AAPL': 275.2,
    'IBM': 145.67,
    'HPQ': 32.5,
    'FB': 195.34,
    'MSFT': 155.82
}


def price_filter(input_dict, price):
    result = {}
    for ticker, stock_price in input_dict.items():
        if stock_price > price:
            result[ticker] = stock_price

    return result


print(price_filter(prices, 150))

assert(price_filter(prices, 150) == {
       'AAPL': 275.2, 'FB': 195.34, 'MSFT': 155.82})

# make dictionay prices over 150
p1 = {key: value for key, value in prices.items() if value > 150}
print(p1)

# min price
min_price = min(zip(prices.values(), prices.keys()))

# max_prirce
max_price = max(zip(prices.values, prices.keys()))

# rank the data
prices_sorted = sorted(zip(prices.values(), prices.keys()))

# make dic of all tech stocks
tech_stokes = {'AAPL', 'IBM', 'FB', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_stokes}
print(p2)


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('v@v.com', '2019-12-16')

print(sub.addr)
print(sub.joined)
print(sub)

print(len(sub))

addr, joined = sub

print(addr)
print(joined)


def compute_cost(records):
    total = 0.0
    for record in records:
        total += record[1] * record[2]
    return total


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost_v2(records):
    total = 0.0
    for record in records:
        s = Stock(*record)
        total += s.shares * s.price
    return total


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

print(a.get('x'))

c = ChainMap(a, b)

print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))


"""
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)
"""


record = ('Dave', 'dave@example,com', '733-555-1212', '847-555-1212')

name, email, *phone_numbers = record

print(phone_numbers)


# __format__() provides hook to python string formatting functionality.

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        super().__init__()
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2012, 12, 21)
print(format(d, 'mdy'))


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


IStream.register(io.IOBase)

f = open('foo.txt')

print(isinstance(f, IStream))

# super used to override any parent methods


class A:

    def __init__(self):
        self.x = 0


class B(A):

    def __init__(self):
        super().__init__()
        self.y = 1


class Pair:

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __repr__(self):
        # !r formatting code and 0 is instance of self
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
        # alternative
        # return 'Pair(%r, %r)'.format(self.x, self.y)

    def __str__(self):
        return '({0.x!s}, {0.x!s})'.format(self)       # !s formatting code


p = Pair(3, 4)
p  # __repr__() output

print(p)  # __str__() output

print('p is {0!r}'.format(p))

print('p is {0}'.format(p))

# format code {0.x} represents x-attribute of argument 0.


# attaching informational metadata to functional argument

def add(x: int, y: int) -> int:
    return x + y

# Python won't type check


help(add)

add.__annotations__

# return multiple values, return tuple


def myfunc():
    return 1, 2, 3


# Use Lambda to sort the list on last name
names = ['David Beasely', 'Brian Jones', 'Reymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))


def add(x, y): return x + y


add(2, 3)
add('hello', 'world')


#
row = ('ACME', 50, 91.5)
print(','.join(str(x) for x in row))
print(*row, sep=',')

print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

for i in range(5):
    print(i)


for i in range(5):
    print(i, end=' ')


# Performing I/O Operations on a String


# Iterate over fixed-sized records


RECORD_SIZE = 32

with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        pass


# manipulating pathnames
path = '/Users/vpatel/Data/data.csv'

# get last component of file
print(os.path.basename(path))

# get the directory name
print(os.path.dirname(path))

# join path components togather
print(os.path.join('tmp', 'data', os.path.basename(path)))

# expand user's home directory
path = '~/Data/data.csv'
print(os.path.expanduser(path))

# split thr file extension
print(os.path.splitext(path))

# for any manipulation of filenames use os.path module instead of trying to cook up your own code.


# test the existance of file
print(os.path.exists('/etc/password'))
# return True or False

# what kind of file
print(os.path.isfile('/etc/password'))

# is directory
print(os.path.isdir('/etc/password'))

# is symbolic link
print(os.path.islink('/usr/local/bin/python3'))

# get file linked to
print(os.path.realpath('/usr/local/bin/python3'))

print(os.path.getsize(path))

print(os.path.getmtime(path))


time.ctime(os.path.getmtime(path))


# Getting Directory Listing

names = os.listdir('somedir')

# get all regular files
names = [name for name in os.listdir(
    'somedir') if os.path.isfile(os.path.join('somedir', name))]

# get all dir
dirnames = [name for name in os.listdir(
    'somedir') if os.path.isdir(os.path.join('somedir', name))]


# decorators


def timethis(func):
    '''
    Decorators that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*arg, **kwargs):
        start = time.time()
        result = func(*arg, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1


print(countdown(100000))


# preserve function metadata when writing decorators such as
# name, doc string, annotations, calling signature

countdown.__name__
countdown.__doc__
countdown.__annotations__
countdown.__wrapped__(1000000)

print(signature(countdown))


def snowflake_retry_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        for _ in range(self.timeout_counter):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.error("Exception during {}".format(func.__name__))
                logging.error(e)
            time.sleep(self.timeout_sleep)
            logging.error("{} failed {} times".format(
                func.__name__, self.timeout_counter))
        return wrapper


# create base class

class BasePythonCallble:
    __metaclass__ = ABCMeta

    def __call__(self, *args, **kwargs):
        return self.execute(*args, **kwargs)

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

#


class BaseRestAPIDataHarvester:
    __metaclass__ = ABCMeta


class BaseS3Uploader:
    __metaclass__ = ABCMeta

    def __init__(self, bucket_name, s3_connection_id, timeout_counter, timeout_sleep):
        super().__init__()
        self.bucket_name = bucket_name
        self.s3_connection_id = s3_connection_id
        self.timeout_counter = timeout_counter
        self.timeout_sleep = timeout_sleep

    @s3_retry_decorator
    def upload_file_to_s3_with_hook(self, filename):
        logging.info('s3 connection id is {}'.format(
            str(self.s3_connection_id)))
        key = ''
        hook = S3Hook()
        hook.load_file()


def make_element(name, value, **attrs):
    keyvals = [' "%s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attr}>{value}</{name}>'.format(
        name=name, attr=attr_str, value=html.escape(value))
    return element


make_element('item', 'Albatross', size='large', quantity=6)


# implement custom iterator pattern that is different than built in func like range(), reversed()
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


# frage
for n in frange(0, 4, 0.5):
    print(n)

# list
list(frange(0, 4, 0.5))


# given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.
# string.ascii_lowercase.index
# Example
# alphabet_position("williamhill")
# Should return 23 9 12 12 9 1 13 8 9 12 12


# swap case

s = "wIlliamHill 2"
result = "WiLLIAMhILL 2"


def swap_case(s):
    # write code here
    return ''.join([i.lower() if i.isupper() else i.upper() for i in s])


#

"""
The goal of this exercise is to convert a string to a new string where each character in the
new string is "(" if that character appears only once in the original string, or ")" if that
character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
"""


"""
In this kata you will create a function that takes a list of non-negative
integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""


def filter_list(l):
    'return a new list with the strings filtered out'
    result = []
    for i in l:
        if isinstance(i, int):
            result.append(i)

    return result


print(filter_list([1, 2, 'a', 'b']))


"""
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata

[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]

"""


def tribonacci(signature, n):
    # your code here
    result = []
    n1, n2, n3 = signature
    count = 0
    while count < n:
        result.append(n1)
        nth = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = nth
        count += 1

    return result


print(tribonacci([1, 1, 1], 10))

#Test.describe("Basic tests")
#Test.assert_equals(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
#Test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
#Test.assert_equals(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
#Test.assert_equals(tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
#Test.assert_equals(tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#Test.assert_equals(tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
#Test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
#Test.assert_equals(tribonacci([1, 1, 1], 1), [1])
#Test.assert_equals(tribonacci([300, 200, 100], 0), [])
#Test.assert_equals(tribonacci([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5])


# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1


def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res


"""
Given two integers a and b, which can be positive or negative,
find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
get_sum(0,-1) == -1
get_sum(0,1) == 1

"""


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


"""
A leap year is exactly divisible by 4 except for century years (years ending with 00).
The century year is a leap year only if it is perfectly divisible by 400. For example,

2017 is not a leap year
1900 is a not leap year
2012 is a leap year
2000 is a leap year
"""

# Python write program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


"""
A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
2, 3, 5, 7 etc. are prime numbers as they do not have any other factors.
ut 6 is not prime (it is composite) since, 2 x 3 = 6.
"""

# Program to check if a number is prime or not

num = 407

# To take input from the user
#num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")


"""
A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.

2, 3, 5, 7 etc. are prime numbers as they do not have any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6.
"""

# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

"""
In the program below, the three numbers are stored in num1, num2 and num3 respectively.
We've used the if...elif...else ladder to find the largest among the three and display it.

# Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

"""


"""
Display the multiplication table of 12.

12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120

"""
# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)


"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
If the function is passed a valid PIN string, return true, else return false.

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False

Test.describe("validate_pin")

Test.it("should return False for pins with length other than 4 or 6")
Test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
Test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
Test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
Test.assert_equals(validate_pin("12345"),False, "Wrong output for '12345'")
Test.assert_equals(validate_pin("1234567"),False, "Wrong output for '1234567'")
Test.assert_equals(validate_pin("-1234"),False, "Wrong output for '-1234'")
Test.assert_equals(validate_pin("1.234"),False, "Wrong output for '1.234'")
Test.assert_equals(validate_pin("-1.234"),False, "Wrong output for '-1.234'")
Test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")
"""


def validate_pin(pin):
    # return true or false
    if pin.isnumeric() and (len(pin) == 4 or len(pin) == 6):
        return True
    else:
        return False


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


def validate_pin(pin):
    return bool(re.match(r'^(\d{4}|\d{6})$', pin))


def validate_pin(pin): return len(pin) in (4, 6) and pin.isdigit()


"""
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

Test.describe("accum")
Test.it("Basic tests")
Test.assert_equals(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
Test.assert_equals(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
Test.assert_equals(accum("MjtkuBovqrU"), "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
Test.assert_equals(accum("EvidjUnokmM"), "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
Test.assert_equals(accum("HbideVbxncC"), "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")
"""


def accum(s):
    # your code
    # return '-'.join((a * i).title() for i, a in enumerate(s, 1))
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


def accum(s):
    output = ""
    for i in range(len(s)):
        output += (s[i]*(i+1))+"-"
    return output.title()[:-1]


def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]

# Finding the Largest or Smallest N Items
# You want to make a list of the largest or smallest N items in a collection.


numbers = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3, numbers))
print(heapq.nsmallest(3, numbers))

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

heap = list(nums)
heapq.heapify(heap)
heap


"""
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
"""


def spin_words(sentence):
    # Your code goes here
    return None


"""
You want to implement a queue that sorts items by a given priority and
always returns the item with the highest priority on each pop operation.
"""


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()
q.pop()
q.pop()
q.pop()


"""
You have two dictionaries and want to find out what they might have in common (same keys, same values, etc.).
"""
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# Find keys in common
a.keys() & b.keys()   # { 'x', 'y' }


# Find keys in a that are not in b
a.keys() - b.keys()   # { 'z' }

# Find (key,value) pairs in common
a.items() & b.items()  # { ('y', 2) }

# Make a new dictionary with certain keys removed
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}

"""
You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items.
If the values in the sequence are hashable,
the problem can be easily solved using a set and a generator.
For example:
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))  # [1, 5, 2, 9, 10]

"""
hashable is immutable objects like string, int, bool, float, tuple
unhashable is list, set and dictionaries which are mutable
This only works if the items in the sequence are hashable. If you are trying to eliminate duplicates in a sequence of unhashable types (such as dicts),
you can make a slight change to this recipe, as follows:
"""


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
list(dedupe(b, key=lambda d: (d['x'], d['y'])))
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

list(dedupe(b, key=lambda d: d['x']))
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]


# slice method
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(1, 3)
print(items(a))


"""
You have a sequence of items, and you’d like to determine the most frequently occurring items in the sequence.
"""
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

"""
As input, Counter objects can be fed any sequence of hashable input items.
Under the covers, a Counter is a dictionary that maps the items to the number of occurrences. For example:
"""
word_counts['not']

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

for word in morewords:
    word_counts[word] += 1

word_counts['eyes']

word_counts.update(morewords)

a = Counter(words)
b = Counter(morewords)

# Combine counts
c = a + b


# Subtract counts
d = a - b

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)


rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))

# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
min(rows, key=itemgetter('uid'))
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
max(rows, key=itemgetter('uid'))


cnopts = pysftp.CnOpts()
with pysftp.Connection('host', username='me', my_private_key='./ssh/id_rsa', cnopts=cnopts):
    print('success')

# Public and Private Methods
# Alarm Clock Class


# Json Exercises

data = {"key1": "value1", "key2": "value2"}

jsonData = json.dumps(data)

print(jsonData)

sampleJson = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sampleJson)
print(data['key2'])

sampleJson = {"key1": "value1", "key2": "value2"}
prettyPrintedJson = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(prettyPrintedJson)

sampleJson = {"id": 1, "name": "value2", "age": 29}

print("Started writing JSON data into a file")
with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")


sampleJson = """{
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data['company']['employee']['payble']['salary'])


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

print("Encode Vehicle Object into JSON")
vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicleJson)

# Question 8: Check whether following json is valid or invalid. If Invalid correct it
{
    "company": {
        "employee": {
            "name": "emma",
            "payble": {
                "salary": 7000
                "bonus": 800
            }
        }
    }
}


def add(x, y):
    return x + y


flie1 = f1.csv
file2 = f2.csv
