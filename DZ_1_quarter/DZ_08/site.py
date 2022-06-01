import re

a = 'file.txt'


def site_parse(ss):
    parse_lst = [r'\d{1,3}\.\d{1,3}\.\d{1-3}\.\d{1,3}',
                 r'\[(.*?)\]',
                 r'\"([A-Z]{3})',
                 r'\s(\/[\w\/]+)',
                 r'\s(\d{3})\s',
                 r'\s\d{3}\s(\d+)']
    return tuple(re.findall(x, str(ss))[0] for x in parse_lst)


if __name__ == '__main__':
    with open(a) as f:
        count, Line = 1100, f.readline()
        while Line and count:
            print(site_parse(Line))


# with open('file.txt', 'r', encoding='utf-8') as fine:
#     print(*fine)
