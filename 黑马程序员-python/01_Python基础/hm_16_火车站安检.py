# 1.定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True

# 3.首先检查是否有车票，如果有，才允许进行 安检
if has_ticket :
    print("车票检查通过，允许进入")

    # 2.定义整型变量 knife_length 表示刀的长度，单位：厘米
    knife_length = int(input("请输入刀的长度(单位：厘米)："))
# 4.安检时，需要检查刀的长度，判断是否超过 20 厘米
    # 4.1如果超过20厘米，提示刀的长度，不允许上车
    if knife_length >= 20 :
        print("你携带的刀具长度为 %d " % knife_length + "厘米，不允许上车")
    # 4.2如果不超过20厘米，安检通过
    else :
        print("你携带的刀具长度为 %d " % knife_length + "厘米，允许上车")
# 5.如果没有车票，不允许进门
else :
    print("车票检查不通过，请先购买车票！")