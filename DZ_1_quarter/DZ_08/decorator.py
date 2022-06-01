# задание № 3
# def type_logger(func):
#     def cube (num):
#         res = func(num)
#         print(f'{func.__name__}({num}: {type(num)}')
#         return res
#     return cube
#
# @type_logger
# def calc_cube(x):
#     return x**3
#
# print(calc_cube(33))

# Задание № 3 усложнённое
def type_logger(func):
    def cube (**kwargs):
        for k, v in kwargs.items():
            print(f'{k} - {v}: {type(v)}')
        return [func(int(v)) for v in kwargs.values()]
    return cube

@type_logger
def calc_cube(x):
    return x**3
print(calc_cube(a=2, b=4, c=6.2, d='8'))
