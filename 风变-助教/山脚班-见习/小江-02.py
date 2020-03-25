a = 5

def hello():
    global a
    # 声明告诉执行引擎用的是全局变量a
    a = 1
    print('In test func: a = %d' % a)

hello()
print('Global a = %d' % a)