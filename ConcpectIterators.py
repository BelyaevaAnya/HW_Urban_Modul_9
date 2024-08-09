# Iterator
# __iter__(self)-получение итератора для перебора
# __next__(self)-переход к следующиму значению и его считывание
# itertools
import sys
from itertools import repeat

ex_iterator = repeat("4", 100000)
print(ex_iterator)
print(f'Размер итератора - {sys.getsizeof(ex_iterator)}')

ex_str = '4' * 100000
print(f'Размер списка - {sys.getsizeof(ex_str)}')

print(sys.getsizeof(ex_str) / sys.getsizeof(ex_iterator))


# Class Iter
class Iter:
    def __init__(self):
        self.first = 'Первый элемент'
        self.second = 'Второй элемент'
        self.third = 'Третий элемент'
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        match (self.i):
            case 1:
                return self.first
            case 2:
                return self.second
            case 3:
                return self.third
            case 4:
                return 'Подсчет закончен'
        raise StopIteration()


obj = Iter()
print(obj)
for val in obj:
    print(val)
try:
    while True:
        val = obj.__next__()
        print(val)
except StopIteration:
    print('Цикл for завершен')


# fibonacci
def fibonacci(n):
    res = []
    a, b = 0, 1
    for _ in range(n):
        res.append(a)
        a, b = b, a + b
    return res


for val in fibonacci(n=10):
    print(val)


# fibonacci class

class Fibonacci:
    """
    Итератор последовательности Фибоначи до N элементов
    """

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a


fib_iter = Fibonacci(20)
print(fib_iter)
for val in fib_iter:
    print(val)
