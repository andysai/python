for i in range(1,10):
    for j in range(1,10):
        print('%d X %d = %d ' % (j,i,i*j),end='  ')
    print('')

print('\n\n')

for i in range(1,10): # 先执行第一个循环，即当i=1时
    for j in range(1,10):
        print('%d X %d = %d ' % (j,i,i*j), end='  ')
        if i == j:
            print('')