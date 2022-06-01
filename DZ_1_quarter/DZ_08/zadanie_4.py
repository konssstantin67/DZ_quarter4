from functools import wraps


def val_checker(one_func):
    def _val_checker(func):
        @wraps(func)
        def wrapp(num):
            if one_func(num):
                res = func(num)
            else:
                raise ValueError(f'не верное число: {num}')
            return res

        return wrapp

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(2))
