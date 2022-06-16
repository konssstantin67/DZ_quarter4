from random import randint
from timeit import timeit

MAX_SIZE = 100
NUMBER_EXECUTIONS = 30000


def primitive_bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for n in range(i):
            if list[n] > list[n + 1]:
                list[n], list[n + 1] = list[n + 1], list[n]

    return list


def smart_bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        flag = True
        for n in range(i):
            if list[n] > list[n + 1]:
                list[n], list[n + 1] = list[n + 1], list[n]
                flag = False

        if flag == True:
            break
    return list


numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]

print(f'изначальный список\n {numbers} \n')
print(f'сортированный спсиок\n {smart_bubble_sort(numbers)}')
print('\nна моём компьютере пришлось подождать около 10 секунд, ждёмс...')

time1 = timeit(f'smart_bubble_sort({numbers})',
               setup='from __main__ import smart_bubble_sort',
               number=NUMBER_EXECUTIONS)

time2 = timeit(f'primitive_bubble_sort({numbers})',
               setup='from __main__ import primitive_bubble_sort',
               number=NUMBER_EXECUTIONS)

print(f'продуманный метод даст результат: {time1}')
print(f'а примитивный в свою очередь даёт такие вот печальные цифры: {time2}')
