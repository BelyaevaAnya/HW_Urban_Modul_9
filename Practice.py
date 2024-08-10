animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']


def gen_repeat(n):
    def repeat(animal_lst):
        return (animal_lst[:2] + '-') * n + animal

    return repeat


test1 = gen_repeat(1)
test2 = gen_repeat(2)
print('Test functions')
print(test1(animal))
print(test2(animal))
# 2
print('Repetitions')
repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)
result = [func(animal) for func in repetitions]
print(result)
# 3
fin_res = [func(x) for x in animals for func in repetitions]
print(fin_res)


# 4
def memoize_f(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции с аргументами {args}, внутренняя память {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Ответ: {mem[args]}'
        else:
            return f'Функция была выполнена ранее, ответ: {mem[args]}'

    return wrapper

@memoize_f
def func_1(a, b):
    print(f'Выполняем функцию с аргументами ({a},{b})')
    return a ** b


print(func_1(3, 5), '\n')
print(func_1(3, 4), '\n')
print(func_1(3, 2), '\n')
print(func_1(3, 5), '\n')
print(func_1(3, 4), '\n')
print(func_1(3, 5), '\n')
