movies = {'妖猫传': ['黄轩', '染谷将太'],
          '无问西东': ['章子怡', '王力宏', '祖峰'],
          '超时空同居':['雷佳音', '佟丽娅']}

a = ['黄轩', '染谷将太', '章子怡', '王力宏', '祖峰', '雷佳音', '佟丽娅']

while True:
    actor = input('【你想查询哪个演员？】\n请输入演员名字,如果不再继续查询请输入n：')
    for movie in movies:
        actors = movies[movie]
    if actor in actors:
        print('【' + actor + '出演了电影' + movie + '】')
        print('----------------------')
    elif actor == 'n':
        print('【欢迎使用本系统，再见】')
        break
    elif actor not in actors:
        print('你输入的名字不在查询范围内！')
        print('----------------------')