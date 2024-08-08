my_f = lambda x: x + 10

print(my_f(x=42))
print(type(my_f))

my_n = [3, 1, 4, 1, 5, 9, 2, 4]
res = map(lambda x: x + 10, my_n)
print(list(res))

my_n = [3, 1, 4, 1, 5, 9, 2, 4]
th_n = [2, 7, 1, 8, 2, 8, 1, 8]
res = map(lambda x, y: x + y, my_n, th_n)
print(list(res))

print(my_f.__name__)


def get_mult_v1(n):
    if n == 2:
        def mult(x):
            return x * 2
    elif n == 3:
        def mult(x):
            return x * 3
    else:
        raise Exception('Я умею умножать только на 2 и 3!')
    return mult


my_n = [3, 1, 4, 1, 5, 9, 2, 4]

by_2 = get_mult_v1(2)
by_3 = get_mult_v1(3)

res2 = map(by_2, my_n)
res3 = map(by_3, my_n)

print(list(res2))
print(list(res3))


def get_mult_v2(n):
    def mult(x):
        return x * n

    return mult


by_5 = get_mult_v2(5)
print(by_5(x=42))

by_10 = get_mult_v2(10)
by_100 = get_mult_v2(100)

print(list(map(by_10, my_n)))
print(list(map(by_100, my_n)))

from pprint import pprint


def matrix(some_list):
    def mult_coloumn(x):
        res = []
        for element in some_list:
            res.append(element * x)
        return res

    return mult_coloumn


my_n = [3, 1, 4, 1, 5, 9, 2, 4]
th_n = [2, 7, 1, 8, 2, 8, 1, 8]

matr_on_my_num = matrix(my_n)

res = map(matr_on_my_num, th_n)
pprint(list(res))

my_n.extend([10, 20, 30])
res = map(matr_on_my_num, th_n)
pprint(list(res))

class Mult:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x * self.n


m_num = [3, 1, 4, 1, 5, 9, 2, 6]
by_100500 = Mult(n=100500)

res = by_100500(x=42)
print(res)

res = map(by_100500, m_num)
print(list(res))