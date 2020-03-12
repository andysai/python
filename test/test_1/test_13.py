import openpyxl

wuliji = [['DELL-R720','2*6C*2','48G(6*8G)','2*1T+2*2T','2'],
           ['DELL-R720','2*6C*2','48G(6*8G)','3*2T''2'],
           ['DELL-R720xd','2*6C*2','32G(4*8G)','2*256G+8*6T','1'],
           ['DELL-C2100,MD1200','','','2'],
           ['Dawning-A620r-H','2*6C*2','48G(6*8G)','2*500G+6*2T','1'],
           ['Dawning-A620r-H','2*6C*2','32G','6*500G','7'],
           ['MacroSAN-MS5020,DSU1516','','','','1'],
           ['MacroSAN-MS3300','','','','2']
           ]
yunzhuji = [['DELL-R720','1C','4G','50G','1'],
            ['DELL-R720','1C','2G','70G','1'],
            ['DELL-R720','2C','2G','40G','1'],
            ['DELL-R720','2C','4G','50G','5'],
            ['DELL-R720','2C','4G','60G','1'],
            ['DELL-R720','2C','4G','70G','1'],
            ['DELL-R720','2C','4G','80G','5'],
            ['DELL-R720','2C','4G','100G','3'],
            ['DELL-R720','2C','4G','150G','1'],
            ['DELL-R720','4C','2G','64G','1'],
            ['DELL-R720','4C','2G','145G','1'],
            ['DELL-R720','4C','8G','80G','1'],
            ['DELL-R720','4C','8G','100G','9'],
            ['DELL-R720','4C','8G','250G','4'],
            ['DELL-R720','4C','16G','50G','2'],
            ['DELL-R720','4C','16G','100G','4'],
            ['DELL-R720','6C','12G','200G','5'],
            ['DELL-R720','8C','16G','100G','1'],
            ['DELL-R720','8C','16G','500G','1'],
            ['DELL-R720','8C','32G','100G','2'],
            ['DELL-R720','8C','32G','2T','1'],
            ['DELL-R720','20C','40G','800G','1'],
            ['DELL-R720','32C','64G','512G+40T','1']
            ]

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '资源统计-物理机'
wb.create_sheet('资源统计-云主机',0)
sheet['A1'] = '型号'
sheet['B1'] = 'CPU'
sheet['C1'] = '内存'
sheet['D1'] = '硬盘'
sheet['E1'] = '数量'

for i in wuliji:
    sheet.append(i)

sheet1 = wb['资源统计-云主机']
sheet1['A1'] = '型号'
sheet1['B1'] = 'CPU'
sheet1['C1'] = '内存'
sheet1['D1'] = '硬盘'
sheet1['E1'] = '数量'
for j in yunzhuji:
    sheet1.append(j)
wb.save('目前在用资源统计-2019-12-02.xlsx')
