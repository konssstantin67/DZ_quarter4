fail = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
its_str = str(fail) # привели в строку что бы привезти всё к одному регистру
lwr_str = (its_str.lower()) # привели к нижнему регистру
slt_str = lwr_str.split() # разбили строку по словам
again_lst = list(slt_str) # перевели строку обратно в список
again_lst[1] = "Игорь" # по индексам меняем имена
again_lst[4] = "Марина"
again_lst[8] = "Николай"
again_lst[10] = "Аэлита"
for i in again_lst: #убираем лишнее
    print(i, end=' ')

print(f'Привет,', again_lst[1]) # у меня привет Игорь выводится в одной строке с командой print(i, end=' '). не могу понять почему
print(f'Привет,', again_lst[4]) # остальные же принты выводятся в столбик как и полагается
print(f'Привет,', again_lst[8])
print(f'Привет,', again_lst[10])