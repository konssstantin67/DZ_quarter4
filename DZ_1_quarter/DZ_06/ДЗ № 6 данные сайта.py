# задание № 1
with open('nginx_logs.txt', 'r', encoding='utf-8') as fine:
    # adress_lst = []
    # for line in f:
    #     ip = line[:line.find(' ')]
    #     typical_request = line[line.find(' "'): line.find(' /d')]
    #     path_file = line[line.find('/d'): line.find('HTTP/1.1')]
    #     final_tuple = (ip, typical_request, path_file)
    #     adress_lst.append(final_tuple)
    #     print(final_tuple)

# задание № 2

    ip = [line[:line.find(' ')] for line in f]
max_ip = max(set(ip), key=ip.count)
print(max_ip, ip.count(max_ip))
