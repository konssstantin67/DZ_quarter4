# дз № 1
def nums_gen(num):
    for n in range(1, num + 1, 2):
        yield n

number = nums_gen(33)
print(next(number))
print(next(number))
print(next(number))
print(*nums_gen(30))  # не могу определится как делать эффетивнее по скорости и затратам ОЗУ
print(list(nums_gen(30)))  # через оператора распаковки или же обертываение в лист и прочее

# дз № 2


num = int(input('Давай сюда уже свое число!: '))
num_gen = (n for n in range(1, num +1, 2))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
