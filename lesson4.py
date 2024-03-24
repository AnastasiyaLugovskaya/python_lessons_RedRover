import math
import functools
import time
import my_calc


# task 4.1


def square(side):
    return side * 4, side ** 2, round(side * math.sqrt(2), 2)


# print(square(int(input('Insert the length of a side: '))))
print("_" * 30)


# task 4.2


def print_kwargs(**kwargs):
    for i, j in kwargs.items():
        print(f'{i}: {j}')


print_kwargs(name='Solasanchik', age=7, color='Grey', eye_color='Yellow')
print("_" * 30)

# task 4.3
my_list = [20, -3, 15, 2, -1, -21]
pos_list = list(filter(lambda x: x >= 0, my_list))
print(pos_list)
print("_" * 30)

# task 4.4

result = functools.reduce(lambda x, y: x * y, pos_list)
print(result)
print("_" * 30)


# task 4.5


def measure_time(func):
    def wrapper(*args):
        start = (time.perf_counter())*1000
        func(*args)
        end = (time.perf_counter())*1000
        return end - start

    return wrapper


@measure_time
def wrapped_func(iterable):
    res = 1
    for i in iterable:
        res += i
    print(res)


lst = [x for x in range(-56, 48)]
print(wrapped_func(lst))
print("_" * 30)

# task 4.6

a, b = 5, 3
print(my_calc.custom_sum(a, b))
print(my_calc.custom_sub(a, b))
print(my_calc.custom_mult(a, b))
print(round(my_calc.custom_div(a, b), 2))
print("_" * 30)
