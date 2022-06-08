#  Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#  Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

# Windows 64 разрядная. Python 3.9


from sys import getsizeof
from random import randint

matrix = []

for i in range(10):
    matrix.append([])
    matrix[i].extend([randint(0, 99) for _ in range(10)])

min_list = []
min_list.extend(matrix[0])

for string in matrix:
    print(f"{('————— ' * len(string)).format(*string)} \n"
          f"{('{:4d} |' * len(string)).format(*string)}"
          )
    i = 0
    for j in string:
        if j < min_list[i]:
            min_list[i] = j
        i += 1

print('min_list \n'
      f"{('————— ' * len(min_list)).format(*min_list)} \n"
      f"{('{:4d} |' * len(min_list)).format(*min_list)} \n"
      f"{('————— ' * len(min_list)).format(*min_list)}"
      )

min_list.sort(reverse=True)
print(f'Максимальный элемент(число) среди минимальных элементов столбцов матрицы: {min_list[0]}')

matrix_size = getsizeof(matrix)
list_size = getsizeof(min_list)
i_size = getsizeof(i)
string_size = getsizeof(string)
j_size = getsizeof(j)

print(
    f'Как оказалось переменные  matrix, string и min_list, каждая занимает {matrix_size} байта \n'  # хотя если ещё чутка подумать ничего удивительного здесь нет
    f'и что вполне логичго переменные  i  и j занимают {i_size} байт каждая\n'
    f'а все вместе переменные занимают {matrix_size + list_size + i_size + string_size + j_size} байт'
    )
