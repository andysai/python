a = 0
while a < 5 :
    i = int(input('请输入0结束循环，你还有5次机会:'))
    a = a + 1
    if i == 0 :
        print('你触发了break语句，导致slse语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')