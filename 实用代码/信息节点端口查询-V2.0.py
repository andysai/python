# 导入tk模块
import tkinter as tk

class MyApp(object):
    def __init__(self, parent):
        self.root = parent
        self.root.title("信息节点端口查询")
        self.frame = tk.Frame(parent)
        self.frame.pack()

        # 1.4 信息点查找端口
        check_message = tk.Button(root, text='1 信息点查找端口', width=16, height=2, command=self.find_message)
        check_message.place(x=100, y=160, anchor="c")

        # 1.5 端口号查找信息点
        check_port = tk.Button(root, text='2 端口号查找信息点', width=16, height=2, command=self.find_port)
        check_port.place(x=240, y=160, anchor="c")

        # 1.6 退出软件
        close = tk.Button(root, text='3 退出', width=16, height=2, command=root.quit)
        close.place(x=380, y=160, anchor="c")

    def hide(self):
        self.root.withdraw()

    def find_message(self):
        self.hide()
        otherFrame = tk.Toplevel()
        otherFrame.title("信息节点端口查询")
        screenWidth= otherFrame.winfo_screenwidth()
        screenHeight = otherFrame.winfo_screenheight()
        width = 480
        height = 320
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        otherFrame.geometry("%dx%d+%d+%d" % (width, height, left, top))
        handler = lambda: self.onCloseOtherFrame(otherFrame)

        l = tk.Label(otherFrame, text="输入节点信息")
        l.pack()
        user_text = tk.Entry(otherFrame, show=None,width=25)
        user_text.pack()

        def Query_information():
            user = user_text.get()
            Information_point = int(user)
            if Information_point > 0 and Information_point <= 49:
                position = Information_point - 1 + 1
                print(f'该信息节点在第一台交换机，对应端口号为:{position}')
            elif Information_point > 49 and Information_point <= 96:
                position = Information_point - 49 + 1
                print(f'该信息节点在第二台交换机，对应端口号为:{position}')
            elif Information_point > 96 and Information_point <= 144:
                position = Information_point - 96 + 1
                print(f'该信息节点在第三台交换机，对应端口号为:{position}')
            elif Information_point > 144 and Information_point <= 192:
                position = Information_point - 144 + 1
                print(f'该信息节点在第四台交换机，对应端口号为:{position}')
            elif Information_point > 192 and Information_point <= 240:
                position = Information_point - 192 + 1
                print(f'该信息节点在第五台交换机，对应端口号为:{position}')
            else:
                print('请输入正确的信息节点!')

        def clear_message():
            user_text.delete(0, 'end')

        # def insert_message():
        #     value = user_text.get()
        #     lb.insert('end', value)
        #     lb.update()

        # 2.4 查找按钮
        check = tk.Button(otherFrame, text='查找', width=10, height=2, command=Query_information)
        check.place(x=96, y=240, anchor="c")

        # lb = tk.Text(otherFrame, height=2,width=25)
        # lb.pack()

        # 2.5 清空按钮
        clear = tk.Button(otherFrame, text='清空', width=10, height=2, command=clear_message)
        clear.place(x=288, y=240, anchor="c")

        # 2.5 关闭按钮
        close = tk.Button(otherFrame, text='关闭', width=10, height=2, command=otherFrame.quit)
        close.place(x=192, y=240, anchor="c")

        # 2.6 返回
        reset = tk.Button(otherFrame, text='返回', width=10, height=2, command=handler)
        reset.place(x=384, y=240, anchor="c")

    def find_port(self):
        self.hide()
        otherFrame = tk.Toplevel()
        otherFrame.title("信息节点端口查询")
        screenWidth= otherFrame.winfo_screenwidth()
        screenHeight = otherFrame.winfo_screenheight()
        width = 480
        height = 320
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        otherFrame.geometry("%dx%d+%d+%d" % (width, height, left, top))
        handler = lambda: self.onCloseOtherFrame(otherFrame)

        l = tk.Label(otherFrame, text="输入交换机编号")
        l.pack()
        user_text1 = tk.Entry(otherFrame, show=None,width=25)
        user_text1.pack()
        l = tk.Label(otherFrame, text="输入端口信息")
        l.pack()
        user_text2 = tk.Entry(otherFrame, show=None,width=25)
        user_text2.pack()

        # 2.2 端口号查询信息点
        def switch_port_message():
            user1 = user_text1.get()
            switch = int(user1)
            user2 = user_text2.get()
            Port_number = int(user2)
            if (Port_number >= 1 and Port_number <= 48) and switch == 1:
                position = Port_number
                print(f'信息点为{position}')
            elif (Port_number >= 1 and Port_number <= 48) and switch == 2:
                position = Port_number + 49 - 1
                print(f'信息点为{position}')
            elif (Port_number >= 1 and Port_number <= 48) and switch == 3:
                position = Port_number + 144 - 1
                print(f'信息点为{position}')
            elif (Port_number >= 1 and Port_number <= 48) and switch == 4:
                position = Port_number + 192 - 1
                print(f'信息点为{position}')
            elif (Port_number >= 1 and Port_number <= 48) and switch == 5:
                position = Port_number + 193 - 1
                print(f'信息点为{position}')
            else:
                print("请输入正确的交换机编号和端口号")

        def clear_message():
            user_text1.delete(0, 'end')
            user_text2.delete(0, 'end')

        # 2.4 查找按钮
        check = tk.Button(otherFrame, text='查找', width=10, height=2, command=switch_port_message)
        check.place(x=96, y=240, anchor="c")

        # 2.5 清空按钮
        clear = tk.Button(otherFrame, text='清空', width=10, height=2, command=clear_message)
        clear.place(x=288, y=240, anchor="c")

        # 2.5 关闭按钮
        close = tk.Button(otherFrame, text='关闭', width=10, height=2, command=otherFrame.quit)
        close.place(x=192, y=240, anchor="c")

        # 2.6 返回
        reset = tk.Button(otherFrame, text='返回', width=10, height=2, command=handler)
        reset.place(x=384, y=240, anchor="c")

    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()

    def show(self):
        self.root.update()
        self.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    width = 480
    height = 320
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2
    root.geometry("%dx%d+%d+%d" % (width, height, left, top))

    app = MyApp(root)
    root.mainloop()
