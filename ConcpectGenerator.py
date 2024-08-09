# Создание генератора
def f_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1


generator_obj = f_generator(10)
print(generator_obj)
# => <generator object f_generator at 0x000001AB7A26CE80>
for i in generator_obj:
    print(i, end=' ')


# => 0 1 2 3 4 5 6 7 8 9

# Генератор Фибоначчи
def fibanacci_1(n):
    res = []
    a, b = 0, 1
    for _ in range(n):
        res.append(a)
        a, b = b, a + b
    return res


def fibanacci_2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def print_f(fib_f):
    print('(1)')
    for val in fib_f:
        print(val, end=' ')
    print('(1)')


fib_f = fibanacci_1(n=10)
print(fib_f)
print_f(fib_f)

fib_f = fibanacci_2(n=10)
print(fib_f)
print_f(fib_f)


# Бесконечный список значений
def fibanacci_3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for val in fibanacci_3():
    print(val)
    if val > 10 ** 6:
        break

# Чтение большого файла
import time

start = time.time()


def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


for line in read_large_file('large_file.txt'):
    print(line)

final = time.time()

print((final - start) * 1000)
