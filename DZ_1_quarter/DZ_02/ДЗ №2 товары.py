price = [44.4, 17.3, 24.5, 99.9, 77.7, 55.3, 87.3, 58.4, 64.2, 48.2, 01.03, 12.00, 76.42, 85.25, 95.12, 23.69, 87.41, 57.35]

for i in (price): # переводим в целое число
    print(f' {int(i//1)} руб. {int(i*100%100):02d} коп.', end=', ')
    #print(id(price))
sort_a = price.sort() # сортируем
print(price)
print(id(price))
rvs_price = list(reversed(price)) # разварачиваем
print(rvs_price)
print(id(rvs_price)) # проверка что теперь это новый список
print(rvs_price[0:5]) # 5 цен по убыванию
print(price[0:5]) # 5 цен по возрастанию