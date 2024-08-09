def is_prime(func):
    def wrapper_prime(*args):
        sum3 = func(*args)
        for i in range(2, (sum3 // 2) + 1):
            if (sum3 % i) == 0:
                print('Составное')
                break
        else:
            print('Простое')
        return sum3
    return wrapper_prime


@is_prime
def sum_three(*args):
    sum3 = 0
    for elem in args:
        sum3 += elem
    return sum3


result = sum_three(2, 3, 6)
print(result)
result = sum_three(5, 5, 5)
print(result)
