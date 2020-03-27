def rewards(month):
    if 0 < month < 6:
        reward = 500
        return reward
    elif 12 > month >= 6:
        reward = month*120
        return reward
    else:
        reward = month*180
        return reward

def info(name,month):
    gain = rewards(month)
    print('%s来了%s个月，获得奖金%s元' % (name,month,gain))

info('大聪',14)