import os

dir_path = 'my_project'
path = ['settings', 'mainapp', 'adminapp', 'authapp']
for a in path:
    os.makedirs(os.path.join(os.curdir, dir_path, a), exist_ok=True)
