import xlrd

class Read_Ex():
    def read_excel_mon_1(self):
        #打开excel表，填写路径
        book = xlrd.open_workbook("陈子林0326早.xlsx")
        #找到sheet页
        table = book.sheet_by_name("Sheet1")
        #获取总行数总列数
        row_Num = table.nrows
        col_Num = table.ncols

        s =[]
        key =table.row_values(0)# 这是第一行数据，作为字典的key值

        if row_Num <= 1:
            print("没数据")
        else:
            j = 1
            for i in range(row_Num-1):
                d ={}
                values = table.row_values(j)
                for x in range(col_Num):
                    # 把key值对应的value赋值给key，每行循环
                    d[key[x]]=values[x]
                j+=1
                # 把字典加到列表中
                s.append(d)
            return s
    def read_excel_after_1(self):
        #打开excel表，填写路径
        book = xlrd.open_workbook("陈子林0326下.xlsx")
        #找到sheet页
        table = book.sheet_by_name("Sheet1")
        #获取总行数总列数
        row_Num = table.nrows
        col_Num = table.ncols

        s =[]
        key =table.row_values(0)# 这是第一行数据，作为字典的key值

        if row_Num <= 1:
            print("没数据")
        else:
            j = 1
            for i in range(row_Num-1):
                d ={}
                values = table.row_values(j)
                for x in range(col_Num):
                    # 把key值对应的value赋值给key，每行循环
                    d[key[x]]=values[x]
                j+=1
                # 把字典加到列表中
                s.append(d)
            return s

    def read_excel_mon_2(self):
        #打开excel表，填写路径
        book = xlrd.open_workbook("陈子林0326早.xlsx")
        #找到sheet页
        table = book.sheet_by_name("Sheet2")
        #获取总行数总列数
        row_Num = table.nrows
        col_Num = table.ncols

        s =[]
        key =table.row_values(0)# 这是第一行数据，作为字典的key值

        if row_Num <= 1:
            print("没数据")
        else:
            j = 1
            for i in range(row_Num-1):
                d ={}
                values = table.row_values(j)
                for x in range(col_Num):
                    # 把key值对应的value赋值给key，每行循环
                    d[key[x]]=values[x]
                j+=1
                # 把字典加到列表中
                s.append(d)
            return s
    def read_excel_after_2(self):
        #打开excel表，填写路径
        book = xlrd.open_workbook("陈子林0326下.xlsx")
        #找到sheet页
        table = book.sheet_by_name("Sheet2")
        #获取总行数总列数
        row_Num = table.nrows
        col_Num = table.ncols

        s =[]
        key =table.row_values(0)# 这是第一行数据，作为字典的key值

        if row_Num <= 1:
            print("没数据")
        else:
            j = 1
            for i in range(row_Num-1):
                d ={}
                values = table.row_values(j)
                for x in range(col_Num):
                    # 把key值对应的value赋值给key，每行循环
                    d[key[x]]=values[x]
                j+=1
                # 把字典加到列表中
                s.append(d)
            return s

if __name__ == '__main__':
    r = Read_Ex()
    mon=r.read_excel_mon_1()
    after=r.read_excel_after_1()
    mon1 = r.read_excel_mon_2()
    after1 = r.read_excel_after_2()
    # 统计所有学员完成的关卡情况
    data = input('请输入日期:') + '号'
    nine_finsh = []
    eight_finsh = []
    seven_finsh = []
    six_finsh = []
    five_finsh = []
    four_finsh = []
    three_finsh = []
    two_finsh = []
    one_finsh = []

    nine_finsh1 = []
    eight_finsh1 = []
    seven_finsh1 = []
    six_finsh1 = []
    five_finsh1 = []
    four_finsh1 = []
    three_finsh1 = []
    two_finsh1 = []
    one_finsh1 = []

    nine_finsh2 = []
    eight_finsh2 = []
    seven_finsh2 = []
    six_finsh2 = []
    five_finsh2 = []
    four_finsh2 = []
    three_finsh2 = []
    two_finsh2 = []
    one_finsh2 = []

    nine_finsh3 = []
    eight_finsh3 = []
    seven_finsh3 = []
    six_finsh3 = []
    five_finsh3 = []
    four_finsh3 = []
    three_finsh3 = []
    two_finsh3 = []
    one_finsh3 = []

    for i in mon:
        if i[data] == 0.0:
            nine_finsh.append(i['昵称'])
        elif i[data] == 1.0:
            eight_finsh.append(i['昵称'])
        elif i[data] == 2.0:
            seven_finsh.append(i['昵称'])
        elif i[data] == 3.0:
            six_finsh.append(i['昵称'])
        elif i[data] == 4.0:
            five_finsh.append(i['昵称'])
        elif i[data] == 5.0:
            four_finsh.append(i['昵称'])
        elif i[data] == 6.0:
            three_finsh.append(i['昵称'])
        elif i[data] == 7.0:
            two_finsh.append(i['昵称'])
        elif i[data] == 8.0:
            one_finsh.append(i['昵称'])

    for i in after:
        if i[data] == 0.0:
            nine_finsh1.append(i['昵称'])
        elif i[data] == 1.0:
            eight_finsh1.append(i['昵称'])
        elif i[data] == 2.0:
            seven_finsh1.append(i['昵称'])
        elif i[data] == 3.0:
            six_finsh1.append(i['昵称'])
        elif i[data] == 4.0:
            five_finsh1.append(i['昵称'])
        elif i[data] == 5.0:
            four_finsh1.append(i['昵称'])
        elif i[data] == 6.0:
            three_finsh1.append(i['昵称'])
        elif i[data] == 7.0:
            two_finsh1.append(i['昵称'])
        elif i[data] == 8.0:
            one_finsh1.append(i['昵称'])


    for i in mon1:
        if i[data] == 0.0:
            nine_finsh2.append(i['昵称'])
        elif i[data] == 1.0:
            eight_finsh2.append(i['昵称'])
        elif i[data] == 2.0:
            seven_finsh2.append(i['昵称'])
        elif i[data] == 3.0:
            six_finsh2.append(i['昵称'])
        elif i[data] == 4.0:
            five_finsh2.append(i['昵称'])
        elif i[data] == 5.0:
            four_finsh2.append(i['昵称'])
        elif i[data] == 6.0:
            three_finsh2.append(i['昵称'])
        elif i[data] == 7.0:
            two_finsh2.append(i['昵称'])
        elif i[data] == 8.0:
            one_finsh2.append(i['昵称'])

    for i in after1:
        if i[data] == 0.0:
            nine_finsh3.append(i['昵称'])
        elif i[data] == 1.0:
            eight_finsh3.append(i['昵称'])
        elif i[data] == 2.0:
            seven_finsh3.append(i['昵称'])
        elif i[data] == 3.0:
            six_finsh3.append(i['昵称'])
        elif i[data] == 4.0:
            five_finsh3.append(i['昵称'])
        elif i[data] == 5.0:
            four_finsh3.append(i['昵称'])
        elif i[data] == 6.0:
            three_finsh3.append(i['昵称'])
        elif i[data] == 7.0:
            two_finsh3.append(i['昵称'])
        elif i[data] == 8.0:
            one_finsh3.append(i['昵称'])

    print('时间:' + data + '\n' + '表名:' + 'sheet1')
    print('完成1关的学员有:' + '早上:' + str(len(one_finsh)) + '个' + ' ' + '下午:' + str(len(one_finsh1)) + '个')
    print('完成2关的学员有:' + '早上:' + str(len(two_finsh)) + '个' + ' ' + '下午:' + str(len(two_finsh1)) + '个')
    print('完成3关的学员有:' + '早上:' + str(len(three_finsh)) + '个'+ ' ' + '下午:' + str(len(three_finsh1)) + '个')
    print('完成4关的学员有:' + '早上:' + str(len(four_finsh)) + '个' + ' ' + '下午:' + str(len(four_finsh1)) + '个')
    print('完成5关的学员有:' + '早上:' + str(len(five_finsh)) + '个' + ' ' + '下午:' + str(len(five_finsh1)) + '个')
    print('完成6关的学员有:' + '早上:' + str(len(six_finsh)) + '个' + ' ' + '下午:' + str(len(six_finsh1)) + '个')
    print('完成7关的学员有:' + '早上:' + str(len(seven_finsh)) + '个' + ' ' + '下午:' + str(len(seven_finsh1)) + '个')
    print('完成8关的学员有:' + '早上:' + str(len(eight_finsh)) + '个' + ' ' + '下午:' + str(len(eight_finsh1)) + '个')
    print('完成9关的学员有:' + '早上:' + str(len(nine_finsh)) + '个' + ' ' + '下午:' + str(len(nine_finsh1)) + '个')

    print('时间:' + data + '\n' + '表名:' + 'sheet2')
    print('完成1关的学员有:' + '早上:' + str(len(one_finsh2)) + '个' + ' ' + '下午:' + str(len(one_finsh3)) + '个')
    print('完成2关的学员有:' + '早上:' + str(len(two_finsh2)) + '个' + ' ' + '下午:' + str(len(two_finsh3)) + '个')
    print('完成3关的学员有:' + '早上:' + str(len(three_finsh2)) + '个'+ ' ' + '下午:' + str(len(three_finsh3)) + '个')
    print('完成4关的学员有:' + '早上:' + str(len(four_finsh2)) + '个' + ' ' + '下午:' + str(len(four_finsh3)) + '个')
    print('完成5关的学员有:' + '早上:' + str(len(five_finsh2)) + '个' + ' ' + '下午:' + str(len(five_finsh3)) + '个')
    print('完成6关的学员有:' + '早上:' + str(len(six_finsh2)) + '个' + ' ' + '下午:' + str(len(six_finsh3)) + '个')
    print('完成7关的学员有:' + '早上:' + str(len(seven_finsh2)) + '个' + ' ' + '下午:' + str(len(seven_finsh3)) + '个')
    print('完成8关的学员有:' + '早上:' + str(len(eight_finsh2)) + '个' + ' ' + '下午:' + str(len(eight_finsh3)) + '个')
    print('完成9关的学员有:' + '早上:' + str(len(nine_finsh2)) + '个' + ' ' + '下午:' + str(len(nine_finsh3)) + '个')
    print('\n')

    # 计没有跟上进度的学员的名称
    for j in after:
        if j[data] == 6.0:
            print('没有完成第三关的人有:' + j['昵称'])
    print('\n')

    for j in after:
        if j[data] == 7.0:
            print('没有完成第二关的人有:' + j['昵称'])
    print('\n')

    for j in after:
        if j[data] == 8.0:
                print('没有完成第一关的人有:' + j['昵称'])
    print('\n')

    print('\n')
    for j in after1:
        if j[data] == 6.0:
            print('没有完成第三关的人有:' + j['昵称'])
        elif j[data] == 7.0:
            print('没有完成第二关的人有:' + j['昵称'])
        elif j[data] == 8.0:
                print('没有完成第一关的人有:' + j['昵称'])