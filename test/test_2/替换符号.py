# 88f8.7217.bdd4
# b40b.44ce.69c7
# mac_address = '88f8.7217.bdd4'
def mac():
    mac_address = input('请输入mac地址:')
    return mac_address

def MAC():
    mac_address = mac()
    mac_address = mac_address.replace('.','-')

    mac_address_list = []

    for i in mac_address:
        mac_address_list.append(i)

    mac_address_list[2:0] = '-'
    mac_address_list[8:0] = '-'
    mac_address_list[14:0] = '-'
    mac_address_str = "".join(str(i) for i in mac_address_list)

    return mac_address_str

a = MAC()
print(a)