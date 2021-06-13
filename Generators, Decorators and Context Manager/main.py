import cProfile
import sys
import time
import random
from contextlib import contextmanager, ContextDecorator

from PiCalc import estimate_pi


# Decorators
def hello(name):
    return f"Hello {name}"


def goodbye(name):
    return f"Goodbye {name}"


def i_am_bob(bob_func):
    return bob_func("Bob")


def parent_func(pick):
    print("Parent print")

    def child_one_func():
        print("Child one print")

    def child_two_func():
        print("Child two print")

    if pick == 1:
        return child_one_func  # Will return reference for function so inner func can be called
    else:
        return child_two_func

# print(hello("Bob"))
# print(goodbye("Bob"))
# Above and below prints the same
# print(i_am_bob(hello))
# print(i_am_bob(goodbye))

child_one = parent_func(1)
child_two = parent_func(2)
print(child_one)  # Reference
print(child_one())  # Inner function called


def time_me(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(f"{func.__name__} finished in {t2 - t1} seconds")
        return result
    return wrapper


@time_me
def big_loop():
    sum_p = 0
    for i in range(100):
        sum_p += i
    return sum_p

# @time_me
# def estimate_pi(p):
#     num_in = 0
#     num_total = 0
#     for point in range(p):
#         x = random.uniform(0, 1)
#         y = random.uniform(0, 1)
#         dist = x**2 + y**2
#         if dist < 1:
#             num_in += 1
#         num_total += 1
#     return 4 * num_in / num_total


estimate_pi = time_me(estimate_pi)
print(estimate_pi)
print(estimate_pi(100000))

print(big_loop)
print(big_loop())


def do_times(times):
    def decorator_do_times(func):
        def wrapper_do_times(*args):
            for _ in range(times):
                result = func(*args)
            return result
        return wrapper_do_times
    return decorator_do_times


@do_times(times=3)
def say_whatever(whatever):
    print(f"I say {whatever}")


say_whatever("Hello there")


# Generators
def csv_reader(file_name):  # Should never raise memory error
    for row in open(file_name, "r"):
        yield row


# (row for row in open(file_name))  # Generator expression, same as above
# Infinite range instead of the normal finite range()
def infinite_range():
    num = 0
    while True:
        yield num
        num += 1


for i in infinite_range():
    print(i, end=" ")
    if i == 500:
        break

print()

inf = infinite_range()
print(next(inf), end=" ")
print(next(inf))

list_comp_squared = [i ** 2 for i in range(10000)]  # Speed
gen_comp_squared = (i ** 2 for i in range(10000))  # Memory
print(sys.getsizeof(list_comp_squared))
print(sys.getsizeof(gen_comp_squared))


class TestClass:
    num1 = 0
    num2 = 0

    def __init__(self, *args):
        self.num1 = args[0]
        self.num2 = args[1]

    def __repr__(self):
        return f'{self.__dict__}'


def class_generator(amount):  # Class generator
    for j in range(amount):
        yield TestClass(j, j + 1)


cg = class_generator(5)
for k in cg:
    print(repr(k))


def two_yield():
    yield "First yield"
    yield "Second yield"


test = two_yield()
print(next(test))
print(next(test))


# Context managers
class OpenFile:  # Custom class
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('__enter__')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, *args):
        print('__exit__')
        self.file.close()


with OpenFile('timelog.txt', 'r') as file:
    print(file.readlines())

with open('timelog.txt', 'r') as f:  # same as above just built in
    print(f.readlines())


# f = open('timelog.txt', 'r')  # Equivalent to above block
# try:
#     print(f.readlines())
# finally:
#     f.close()


@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()


with open_file('timelog.txt', 'r') as f:
    print(f.read())


# class MakePara(ContextDecorator):
#     def __enter__(self):
#         print('<p>', end=" ")
#         return self
#
#     def __exit__(self, *arg):
#         print('</p>')
#         return False
#
#
# @MakePara()
# def emit_html(msg):
#     print(msg, end=" ")
#
# emit_html('This is decorated')
