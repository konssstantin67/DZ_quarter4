from random import randint
from timeit import timeit

MAX_SIZE = 100
NUMBER_EXECUTIONS = 30000

def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2

    left_part = array[:mid]
    right_part = array[mid:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    return merge_list(left_part, right_part)


def merge_list(list_1, list_2):
    result = []
    left = 0
    right = 0
    while left < len(list_1) and right < len(list_2):
        if list_1[left] <= list_2[right]:
            result.append(list_1[left])
            left += 1
        else:
            result.append(list_2[right])
            right += 1

    result += list_1[left:]
    result += list_2[right:]
    return result


numbers = [randint(0, 100) for _ in range(MAX_SIZE)]

print('изначальный список', numbers, '\n')
print('сортированный спсиок', merge_sort(numbers))
time = timeit(f'merge_sort({numbers})',
               setup='from __main__ import merge_sort',
               number=NUMBER_EXECUTIONS
              )

print('ну и до кучи выведем время работы сортировки:', time)