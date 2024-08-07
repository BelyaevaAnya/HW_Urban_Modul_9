def by_3(x):
    return x * 3


def is_odd(x):
    return x % 2


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = filter(is_odd, my_numbers)
print(list(result))
result = map(by_3, filter(is_odd, my_numbers))
print(list(result))
collection = [3, 1, 4, 1, 5, 9, 2, 6]
list_comp_1 = [x * 2 for x in collection]
print(list_comp_1)
result = [x * 3 for x in collection]
print(result)
list_comp_2 = [x * 2 for x in collection if x > 5]
print(list_comp_2)
list_comp_2 = [x * 3 for x in my_numbers if x % 2]
print(list_comp_2)
list_comp_3 = [x * 2 if x > 2 else x * 10 for x in collection]
print(list_comp_3)
my_numbers = ['A', 1, 4, 'B', 5, 'C', 2, 6]
result = [x if type(x) == str else x * 5 for x in my_numbers]
print(result)
collection2 = [3, 1, 4, 1, 5, 9, 2, 6]
list_comp_4 = [x * y for x in collection for y in collection2]
print(list_comp_4)
list_comp_4 = [x * y for x in collection for y in collection2 if x % 2]
print(list_comp_4)
list_comp_4 = [x * y for x in collection for y in collection2 if x % 2 and y // 2]
print(list_comp_4)
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = {x for x in my_numbers}
print(result)
they_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = {x: x ** 2 for x in they_numbers}
print(result)
