class Stationery:
    def __init__(self, title):
        self.title = title

    def drow(self):
        print('Запуск отрисовки')


class pen(Stationery):
    def drow(self):
        print(f'рисуем ручкой', self.title)


class pencil(Stationery):
    def drow(self):
        print(f'рисуем карандашом', self.title)


class handle(Stationery):
    def drow(self):
        print(f'рисуем маркером', self.title)


p = pen('parker')
pl = pencil('erich krause')
h = handle('марекер без названия')
pl.drow()