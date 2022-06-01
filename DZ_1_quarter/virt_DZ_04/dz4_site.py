from requests import get, utils
from decimal import Decimal
def currency_rates (code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    coin = {}
    for n in content.split('</Value>'):
        i = n.split('</CharCode>')[0][-3:]
        nominal = n.split('</Nominal>')[0][-5:] # проверка валюты на номинал (на цб рф есть валюта которая берется не за 1 еденицу а допустим за 10 или 100 едениц)
        # выкидываем лишние символы оставляем только цифры и преобразуем строку в цифры
        nominal = int(nominal.replace('l', '').replace('>', '').replace('nal', '').replace('al', '')\
                      .replace('na', '').replace(' ', '').replace('a', '').replace('Curs', '').replace('nal>', ''))
        f = str(round((int(n[-7:-1].replace(',', ''))/1000)/nominal, 4)) # выкидываем запятые оставшиеся цифры делим на 1000
        # получаем число типо флоат (две цифры целого остальное после запятой) делим это на номинал,
        # тк есть числа которые с кучей символов поле запятой округляем всё это дело до 4 символом после запятой и оборачиваем это в строку
        coin[i] = f if i.isalpha() else None
        print(coin)
    code = code.upper()
    if coin.setdefault(code) == None:
        print('Ошибочная валюта')
    else:
        # price = Decimal(coin[code].replace('.', '.')).quantize(Decimal('00.01'))
        print(f'{coin} = RU.')
currency_rates(input('введите валюту: '))




