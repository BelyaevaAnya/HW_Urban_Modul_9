# Декоратор
def null_generator(func):
    return func


def greet():
    return 'Hello!'


greet = null_generator(greet)
print(greet())


# @ декоратор
def null_generator(func):
    return func


@null_generator
def greet():
    return 'Hello!'


print(greet())

print('Upper')


# почему нужно внутри декоратора определить функцию
def uppercase(func):
    def wrapper():
        orig_res = func()
        mod_res = orig_res.upper()
        return mod_res

    return wrapper


@uppercase
def greet():
    return 'Hello!'


greet_dec = uppercase(greet)
print(greet())
print('upper object')
print(greet_dec())
#
print('New upper')


def uppercase1(func):
    orig_res = func()
    mod_res = orig_res.upper()
    return mod_res


@uppercase
def greet1():
    return 'Hello!'


print(greet1())

from time import time
from sys import set_int_max_str_digits


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time()
        res_s = func(*args, **kwargs)
        ended_at = time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return res_s

    return surrogate


def digits1(*args):
    total = 1
    for num in args:
        total *= num ** 5000
    return len(str(total))


@time_track
def digits2(*args):
    total = 1
    for num in args:
        total *= num ** 5000
    return len(str(total))


set_int_max_str_digits(100000)
res = digits1(3141, 5926, 2718, 2818)
print(res)
# => 70771
set_int_max_str_digits(100000)
res = digits2(3141, 5926, 2718, 2818)
print(res)
# =>
# Функция работала 0.02 секунд(ы)
# 70771
