import hashlib

string = input('Введите строку, состоящую из латинских букв').lower()
sum_substring = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_substring.add(hash_str)

print(f'{len(sum_substring)} различных подстрок в строке {string}')
