from tkinter import *

root=Tk()
v=StringVar()

lb=Listbox(root,listvariable=v)
for item in ['python','tkinter','widget']:
    lb.insert(END,item)

lb.insert(ACTIVE,'linux','windows','unix')
print(v.get())
v.set(('1000','200'))

lb.pack()

root.mainloop()
