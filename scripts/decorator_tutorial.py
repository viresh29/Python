import time
from functools import wraps


def timethis(func):
    '''
    Decorator that reports the time
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@timethis
def countdown(n: int):
    '''
    Counts Down
    '''
    while n > 0:
        n -= 1


countdown(1000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)


"""def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return ('lorem ipsum, {} dolor sit amet'.format(name))


print(get_text('john'))


def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()

print(my_person.get_fullname())




def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name

print(get_text("John"))
print(get_text.__name__)
print(get_text.__doc__)
print(get_text.__module__)

"""


def example_function():
    print("Example Function Called")


some_variable = example_function

some_variable()


def decorator_example(func):
    print("DEcorator Called")

    def inner_function(*args, **kwargs):
        print("Calling the function")
        func(*args, **kwargs)
        print("Functions execution is over")
    return inner_function


@decorator_example
def some_function():
    print("Executing function")


some_function()


"""
def area_square(length):
    try:
        print(length**2)
    except TypeError:
        print("area_square only takes numbers as the argument")


def area_circle(radius):
    try:
        print(3.142 * radius**2)
    except TypeError:
        print("area_circle only takes numbers as the argument")


def area_rectangle(length, breadth):
    try:
        print(length * breadth)
    except TypeError:
        print("area_rectangle only takes numbers as the argument")
"""


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"{func.__name__} only takes numbers as the argument")
    return inner_function


@exception_handler
def area_square(length):
    print(length * length)


@exception_handler
def area_circle(radius):
    print(3.14 * radius * radius)


@exception_handler
def area_rectangle(length, breadth):
    print(length * breadth)


area_square(2)
area_circle(2)
area_rectangle(2, 4)
area_square("some_str")
area_circle("some_other_str")
area_rectangle("some_other_rectangle", "xx")
