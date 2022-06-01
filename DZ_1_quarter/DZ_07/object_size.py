import json
import os

size = {}

for root, dirs, files, in os.walk('my_project'):
    for file in files:
        k_dict = os.stat(os.path.join(root, file)).st_size // 10 * 10 + 10
        file_ext = file.rsplit('.')[-1]
        if k_dict in size:
            size[k_dict][1].append(file_ext)
            size[k_dict] = (size[k_dict][0] + 1, list(set(size[k_dict][1])))
        else:
            size.setdefault(k_dict, (1, [file_ext]))
result = {k: size[k] for k in sorted(size.keys())}

with open('result.json', 'w') as a:
    json.dump(result, a)
with open('result.json', 'r') as a:
    print(json.load(a))
