from itertools import zip_longest

# задание № 1
# import json
#
# with open('users.csv', 'r', encoding='utf-8') as name, \
#     open('hobby.csv', 'r', encoding='utf-8') as hobby:
#     name = name.read().splitlines()
#     hobby = hobby.read().splitlines()
#
# if len(name) < len(hobby):
#     print(1)
# else:
#     users = dict(zip_longest(name,hobby, fillvalue=None))
#     with open('dict_users.txt', 'w', encoding='utf-8') as f:
#         json.dump(users, f, ensure_ascii=False)

#  задание № 2
with open('users.csv', 'r', encoding='utf-8') as name, \
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
    name = name.read().splitlines()
    hobby = hobby.read().splitlines()

gen_users = ((name, hobby) for name, hobby in zip_longest(name, hobby, fillvalue=None))

with open('users1.txt', 'w', encoding='utf-8') as f:
    for i in gen_users:
        f.write(f'{i[0]}: {i[1]}\n')