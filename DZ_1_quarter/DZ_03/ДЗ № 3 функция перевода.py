def translet(number): # принимаем число
    var = {
        'zero': "ноль",
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if number in var: # проверяем есть ли число в словаре
        print(var [number])
    else:
        print('Erorr')
translet('five') # вводим число

#_________________________________________ЧАСТЬ ВТОРАЯ_______________________________________

def translet_adv(number):
    var = dict(zero="ноль", one='один', two='два', three='три', four='четыре', five='пять', six='шесть', seven='семь',
               eight='восемь', nine='девять', ten='десять')
    if number in var:
        print(var[number])
    else: # до этого все тоже самое, а здесь приводим ключи к верхнему регистру
        var = {k.title(): var[k] for k in var}
        print(var[number].title()) # делаем выводимое значение с заглавной буквы

translet_adv('Seven')
