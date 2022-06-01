class worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name, self.surname, self.position, self._income = name, surname, position, {'bonus': bonus,
                                                                                         'salary': salary}


class Position(worker):
    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def a(self):
        return f'{self._income["salary"]}'

    def b(self):
        return f'{self._income["bonus"]}'

    def full_name(self):
        return f'{self.name} {self.surname}'

    def total_income(self):
        return f'{self._income["salary"] + self._income["bonus"]}'


work = Position('Владимир', 'Путин', 'президент', 12792, 200)
print(work.name, work.surname, work.total_income())
print(
    f'наш "любимый" {work.position} {work.full_name()} должен получать {work.a()} рублей, и премию {work.b()} рублей, '
    f'что в купе составляет {work.total_income()} и не копейкой больше!')
