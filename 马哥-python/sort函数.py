# sorted
lst = [1,2,5,4,2,3,5,6]

def sort(iterable,key=lambda x,y:x>y,reverse=False):
    ret = []
    for x in iterable:
        for i,y in enumerate(ret):
            flag = key(x,y) if reverse else key(y,x)
            if flag :
                ret.insert(i,x)
                break
        else:
            ret.append(x)
    return ret
print(sort(lst,lambda x,y:x>y))