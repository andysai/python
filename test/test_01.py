hdt = ['sai','andy','king','alice','amy','green']
utkta = input('请输入无法赴约的宾客名字：')
if utkta in hdt:
    print(hdt)
    hdt.remove(utkta)
    print('很遗憾，{}因为有其他紧急的事情需要处理，无法赴约！'.format(utkta))
    print(hdt)
