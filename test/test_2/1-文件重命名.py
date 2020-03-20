import os,sys

list = ['ITSM-L4-006-001-2017-001服务报告(清溪党政办2017年7-9月份).docx','ITSM-L4-006-002 服务报告管理表.xls']
# 指定文件路径
#path = r'F:\ISO-2019资料\ISO20000-运维(2019年)\ITSM-L2-006服务报告管理\清溪党政办'
path = r'D:\study\python\test\test_2'
for i in os.listdir(path):
    if i == list[0]:
        #print(i)
        for j in range(1,3):
            if j == 1:
                pass
                #print('ITSM-L4-006-00'+ str(j) + '-2019-00' + str(j) + '服务报告(网络中心2019年' + str(j+6) + '-' + str(j+8) + '月份).docx')
            elif j == 2:
                pass
                #print('ITSM-L4-006-00' + str(j) + '-2019-00' + str(j) + '服务报告(网络中心2019年' + str(j + 8) + '-' + str(
                #    j + 10) + '月份).docx')
    if i == list[1]:
        print(i)
        for j in range(1, 3):
            if j == 1:
                pass
                print('ITSM-L4-006-00' + str(j) + ' 服务报告管理表.xls')
            elif j == 2:
                pass
                # print('ITSM-L4-006-00' + str(j) + '-2019-00' + str(j) + '服务报告(网络中心2019年' + str(j + 8) + '-' + str(
                #    j + 10) + '月份).docx')


# 列出目录
#for file in os.listdir(path):
#    os.rename(os.path.join(path,file),os.path.join(path,new_name))