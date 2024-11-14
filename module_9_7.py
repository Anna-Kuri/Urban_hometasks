from typing import Callable
def prime_check(number: int) -> None:
    if number == 1:
        print('Число 1 - натуральное число, не относящееся ни к простым, ни к составным числам')
    else:
        flag = 0
        for i in range(2, number // 2 +1):
            if number % i == 0:
                flag += 1
        if flag == 0:
            print('Простое')
        else:
             print('Составное')

def is_prime(func: Callable) -> Callable:
    def wrapper(*args: int) -> int:
        number = func(*args)
        prime_check(number)
        return number
    return wrapper

@is_prime
def sum_three(*args) -> int:
    return sum(args)


result = sum_three(2, 3, 6)
print(result)