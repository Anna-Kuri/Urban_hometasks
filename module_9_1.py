from typing import Callable


def apply_all_func(int_list: int | float, *functions: Callable) -> dict:
    result = {}

    for function in functions:
        result[function.__name__] = function(int_list)

    return result

    
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
