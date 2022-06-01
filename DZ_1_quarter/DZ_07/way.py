import os

way = {}
with open('config.yaml') as a:
    line = dict(map(str.split, a.readlines()))
    print(line)
dir_path = line.pop('base')
for k,v, in line.items():
    os.makedirs(os.path.join(os.curdir, dir_path, k), exist_ok= True)
    print(f'создана папка {k}')
    for i in v.split(','):
        with open(os.path.join(os.curdir,dir_path,k,i), 'w') as l:
            print(f'создан файл - {i} в папке {k}')
