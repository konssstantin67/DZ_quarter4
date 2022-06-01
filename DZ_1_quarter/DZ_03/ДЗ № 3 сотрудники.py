# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?
# def thesaurus(item):
#     worker = str(item)
#     workers = dict()
#     a = []
#     for i in item.split(', '):
#         worker1= i[0]
#         # print(i[0])
#         for item in (workers):
#             print(item)
#         else:
#             workers.update(k=worker1,v=item)
#         print(workers)
#
#
# thesaurus('иван, илья, петр, ирина, том, форд, джим, дмитрий, федор, тимофей')









def thesaurus(item):
    worker = str(item)
    workers = dict()
    a = []
    b = []
    for i in item.split(', '):
        worker1= i[0]
        # print(i[0])
        for item in (workers):
            print(item)
        else:
            a.append(worker1)
            for i in (a):
                b = set (a)
                print (b)
    # if b[0]==item[0]:
    #     workers.update(k=a,v=item)
    #     print(workers)



thesaurus('иван, илья, петр, ирина, том, форд, джим, дмитрий, федор, дарья, дионис, тимофей')
