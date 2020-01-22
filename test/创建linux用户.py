name = [
'xfu',
'hym',
'ljm',
'lss',
'pwj',
'lxg',
'lhb',
'lhh',
'chenfan',
'xyk',
'czl',
'cll',
'yrx',
'ljg',
'ck',
'lzz',
'lcg',
'lhr',
'lcl',
'zwl',
'cxb',
'lyh',
'fy',
'zls',
'lsz',
'ly',
'qwg',
'hya',
'qzj']
password = [
'15481X',
'143345',
'142729',
'251529',
'042786',
'232219',
'302735',
'174374',
'01437X',
'095611',
'187518',
'053837',
'174568',
'135358',
'054430',
'204014',
'010550',
'030391',
'103716',
'075378',
'167554',
'237550',
'230050',
'152098',
'17801X',
'097554',
'050431',
'142213',
'216936']

# 将列表转换为字典
dictionary = dict(zip(name, password))
#print(dictionary)
# 创建用户
for i in dictionary.keys():
        useradd = 'useradd -g companyftp -s /sbin/nologin -d /home/' + i + ' ' + i
        #print(useradd)
# 修改用户密码为身份证后6位
for k,p in dictionary.items():
    passwd = 'echo "' + p + '" | passwd --stdin ' + k
    print(passwd)
# 修改目录权限
for e in dictionary.keys():
    chage = 'chmod a-w /home/' + e
    #print(chage)
# 设置磁盘限额容量
for d in dictionary.keys():
    userrongliang = 'setquota -u ' + d + ' 104857600 104857600 0 0 /home'
    #print(userrongliang)