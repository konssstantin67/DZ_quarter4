from itertools import zip_longest


class matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        print(f'▬' * (len(self.args[0]) * 3 + 1))
        for items in self.args:
            for i in items:
                print(f'█{i:^4}', end='')
            print('█')
            print(f'▬' * (len(self.args[0]) * 3 + 1))
        return f'~' * (len(self.args[0]) * 5 + 1)

    def __add__(self, other):
        sum_matrix = []
        for items_self, items_other in zip_longest(self.args, other.args, fillvalue=0):
            result = list(map(lambda x: x[0] + x[1], zip_longest(items_self, items_other, fillvalue=0)))
            sum_matrix.append(result)
        return matrix(sum_matrix)


matrix_s = matrix([[15, 23], [16, 24]])
matrix_m = matrix([[14, 22, 30], [15, 235, 31], [17, 25, 33]])
matrix_l = matrix([[18, 256], [19, 27], [2055, 28], [21, 29]])
matrix_xl = matrix([[18, 26, 19, 27], [2550, 28, 21, 29]])

# print(matrix_s)
# print(matrix_m)
# print(matrix_l)
# print(matrix_xl)
print(matrix_s + matrix_xl, '\n', type(matrix_s + matrix_xl))
