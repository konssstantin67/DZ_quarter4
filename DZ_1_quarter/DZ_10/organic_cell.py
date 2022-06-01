class cell:
    def __init__(self, args):
        self.args = args

    def __add__(self, other):
        return cell(self.args + other.args)

    def __sub__(self, other):
        return cell(self.args - other.args) if self.args - other.args >= 0 \
            else f'число не верное, разность равна нулю или меньше'

    def __mul__(self, other):
        return cell(self.args * other.args)

    def __floordiv__(self, other):
        return cell(self.args // other.args)

    def __truediv__(self, other):
        return cell(self.args // other.args)

    def worker(self, i):
        for _ in range(self.args // i):
            print('*' * i)
        print('*' * (self.args % i))


cell_1 = cell(32)
cell_2 = cell(44)
cell_3 = cell(10)
 
print((cell_1 + cell_2).args)
print((cell_1 - cell_2))
print((cell_1 - cell_3).args)
print((cell_1 // cell_3).args)
print((cell_1 / cell_3).args)
print((cell_1 * cell_2).args, type(cell_1 * cell_2))
cell_1.worker(7)
