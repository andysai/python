import urllib.request
import json
# import msvcrt

kd_dict = {1:'shentong',2:'youzhengguonei',3:'yuantong',4:'shunfeng',5:'yunda',6:'zhongtong',7:'tiantian',8:'debang',9:'jingdongwuliu',0:"退出"}

def Check():
    while True :
        print("仅支持以下快递公司查询：")
        print("1.申通")
        print("2.EMS邮政")
        print("3.圆通")
        print("4.顺丰")
        print("5.韵达")
        print("6.中通")
        print("7.天天")
        print("8.德邦")
        print("9.京东物流")
        print("0.退出\n")

        choose = int(input("请输入你选择的快递公司："))
        while choose not in range(0,10) :
            choose = int(input("抱歉暂不支持此快递公司，请重新选择："))
        if choose == 0 :
            print("感谢使用！\n")
            break
        kd_num = input("请输入快递单号：")
        url = "https://www.kuaidi100.com/?from=openv" % {kd_dict[choose], kd_num}
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        status = target['status']
        if status == '200' :
            data = target['data']
            data_len = len(data)
            for i in range(data_len) :
                print("\n时间：" + data[i]['time'])
                print("\n状态：" + data[i]['context'] + "")
            print("感谢使用\n")
            break
        else :
            print("输入有误，请重新输入！")

if __name__ == '__main__' :
    while True :
        Check()
        out = input("按任意数字退出(其他键继续).....")
        if out >= '0' and out <= '9' :
            break
        else :
            print("\n")
            continue
