# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
numbers = range(1000) # создаем диапозон от 0 до 1000
figure = [] # создаем пустой список
#print (list(numbers)) # просто проверка себя
i =0
for i in range(1,len(numbers), 2): # если значение (i) есть в диапазоне от 1 до длины списка numbers, то берем нечетные числа
    number = i**3 # берем полученые нечетные числа и возводим в тртью степерь (куб)
    figure.append(number) # добавляем наши кубы в список figure
    # print(number)
ss = []
sum1 =0
for num in figure: # если число есть в списке figure
    i = num
    while num !=0: # если это число не ровно 0
        sum1 += num % 10 # то мы берем это число делим на 10 и остаток после запятой записываем в перменную
        #print(sum1)
        num = num // 10 # тоже самое только берем целую часть
        # print(num)
    if sum1 % 7 == 0: # если остаток числа делится на 7 без остатка добавляем это число в список ss
        ss.append(i)
    sum1 = 0
print(sum(ss))
