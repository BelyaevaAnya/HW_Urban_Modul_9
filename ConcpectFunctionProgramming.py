def get_rus_names():
    return ['Ваня', 'Машка', 'Игорек', ]

def get_brit_names():
    return ['Oliver', 'Jack', 'Harry']

def adder(args):
    res = 0
    for num in args:
        res += num
    return res

def multiplier(args):
    res = 1
    for num in args:
        res *= num
    return res

def process_numbers(numbers, function):
    result = function(numbers)
    print(f'Получилось: {result}')

def mul_by_2(x):
    return x * 2

def is_odd(x):
    return x % 2

get_rus_names()
print(type(get_rus_names()))

print(get_rus_names.__name__)
my_func = get_rus_names
print(my_func())
print(my_func.__name__)

name_getters = [get_brit_names, get_rus_names]
for name_getter in name_getters:
    print(name_getter())

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
process_numbers(numbers=my_numbers, function=adder)
process_numbers(numbers=my_numbers, function=multiplier)

result = map(mul_by_2, my_numbers)
print(result)
print(list(result))

result = filter(is_odd, my_numbers)
print(result)
print(list(result))