def apply_all_func(int_list, *functions):
    call_func_dict = {}
    for func in functions:
        results = func(int_list)
        call_func_dict.update({f'{func.__name__}': results})
    return call_func_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
