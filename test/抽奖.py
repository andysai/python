from tkinter import *
import hashlib

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("抽奖程序")      #窗口名
        self.init_window_name.geometry('1068x680+10+10')                 #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置

        # self.init_window_name["bg"] = "pink"                            #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.9)                  #虚化，值越小虚化程度越高

def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window) # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()