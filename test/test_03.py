def priates():
    emperors = {'白胡子':'爱德华','百兽':'凯多','红发':'香克斯','big mom':'夏洛特'}
    for k,v in emperors.items():
        if k == '白胡子':
            continue
        print('四皇之一：%s%s' % (k,v))
    else:
        print('四皇是如皇帝般')
    return '四皇'

print(priates())