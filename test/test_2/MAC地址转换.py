import tkinter as tk
from tkinter import *

# 面向对象的编程思想
class APP:
    def __init__(self, master):
        # 自动选定大小与位置
        self.frame = tk.Frame(master)
        self.frame.pack()

        # 窗口内容设置
        l = tk.Label(self.frame,
                     text='欢迎使用MAC地址转换工具',  # 标签的文字
                     font=('Arial', 12),  # 字体和字体大小
                     width=25, height=2  # 标签长宽
                     )
        l.pack()

        # 设置一个文本框
        self.user_text = tk.Entry(self.frame,font=('Arial', 12))
        self.user_text.pack()

        # 新建一个按钮
        # 自动设置按钮的位置
        self.hi_there = tk.Button(self.frame,
                                  text="转换",
                                  command=self._introduce)
        self.hi_there.pack()

        self.listb = Listbox(self.frame,height=2,width=25)
        self.listb.pack()

    def getuser(self):
        return self.user_text.get()

    def _introduce(self):
        mac_address = self.getuser()

        mac_address_list = []

        for i in mac_address:
            mac_address_list.append(i)

        mac_address_list[2:0] = '-'
        mac_address_list[8:0] = '-'
        mac_address_list[14:0] = '-'
        mac_address_str = "".join(str(i) for i in mac_address_list).replace('.', '-')

        self.listb.delete(0)
        self.listb.insert(0,mac_address_str)

def main():
    window = tk.Tk()
    window.title('MAC地址转换')
    window.geometry('250x250')
    app = APP(window)

    window.mainloop()

if __name__ == '__main__':
    main()