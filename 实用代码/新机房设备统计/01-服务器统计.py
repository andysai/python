lists_24C = []
lists_40C = []
lists_64C = []
# 统计DELL R720服务器
# 24C
f = open('DELL R720 24C.txt', 'r', encoding='UTF-8')
for i in f.readlines():
    list = i.strip('\n')
    lists_24C.append(list)
f.close()

normal = lists_24C.count('正常')
free = lists_24C.count('空闲') + lists_24C.count('关机')

print(f'目前正常使用的DELL R720 24C服务器有{normal}台,空闲的有{free}台')

# 40C
f = open('DELL R720 40C.txt', 'r', encoding='UTF-8')
for i in f.readlines():
    list = i.strip('\n')
    lists_40C.append(list)
f.close()

normal = lists_40C.count('正常')
free = lists_40C.count('空闲') + lists_40C.count('关机')

print(f'目前正常使用的DELL R720 40C服务器有{normal}台,空闲的有{free}台')

# 统计DELL R910 服务器
f = open('DELL R910 64C.txt', 'r', encoding='UTF-8')
for i in f.readlines():
    list = i.strip('\n')
    lists_64C.append(list)
f.close()

normal = lists_64C.count('正常')
free = lists_64C.count('空闲') + lists_64C.count('关机')

print(f'目前正常使用的DELL R910 64C服务器有{normal}台,空闲的有{free}台')