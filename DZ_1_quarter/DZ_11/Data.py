# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
from pydantic import validator
class DateTime(object):
    def __init__(self, day=10, month=None, year=2000):
        if month is None:
            a = {'01': 'январь',
                     '02': 'февраль',
                     '03': 'март',
                     '04': 'апрель',
                     '05': 'май',
                     '06': 'июнь',
                     '07': 'июль',
                     '08': 'август',
                     '09': 'сентябрь',
                     '10': 'октябрь',
                     '11': 'ноябрь',
                     '12': 'декабрь'}
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(self, string_date):
        day, month, year = map(int, string_date.split('-'))
        myDate = self(day, month, year)
        return day, month, year

    # @validator('month')
    # def month_str(self, month):
    #     for i in month:
    #         print(k,v)
    #     return f'не верный месяц'




dateObj = DateTime.from_string('20-12-1995')
print(dateObj)
