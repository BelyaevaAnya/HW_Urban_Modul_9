from time import time
from sys import set_int_max_str_digits


def func_gen_dec(precision):
    def dec(func):
        def wrapper(*args, **kwargs):
            started_at = time()
            res_s = func(*args, **kwargs)
            ended_at = time()
            elapsed = round(ended_at - started_at, precision)
            print(f'Функция работала {elapsed} секунд(ы)')
            return res_s

        return wrapper

    return dec


@func_gen_dec(precision=6)
def digits2(*args):
    total = 1
    for num in args:
        total *= num ** 5000
    return len(str(total))


set_int_max_str_digits(10 ** 5)

# time_track_precision_6 = func_gen_dec(precision=8)
# dig = time_track_precision_6(digits2)
# resu = digits2(3141, 5926, 2718, 2818)
# print(resu)
res = digits2(3141, 5926, 2718, 2818)
print(res)
