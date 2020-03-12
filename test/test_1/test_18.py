from tkinter import *
from tkinter import messagebox  # python3.0的messagebox，属于tkinter的一个组件

top = Tk()
sw = top.winfo_screenmmwidth() # 获取屏幕宽度
sh = top.winfo_screenmmheight() # 获取屏幕高度
x = (sw - 100) / 2
y = (sh - 100) / 2
top.title("抽奖程序")
top.geometry("%dx%d+%d+%d" %(1068,680,x,y))
# messagebox.showinfo("Python command", "人生苦短、我用Python")
Button(top, text="确认", width=25, height=2, bg="red", relief="raised").pack()
Button.place = (10,10)
#Button(top, text="设置按钮状态", width=21, state="disable").pack()
#Button(top, text="设置bitmap放到按钮左边位置", compound="left",bitmap="error").pack()

top.mainloop()