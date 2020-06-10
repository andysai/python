import tkinter
from tkinter.scrolledtext import *
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


root = tkinter.Tk(className=" Another way to create a Scrollable text area")
textPad = ScrolledText(root, width=50, height=40)

textPad.insert(tkinter.constants.END, chars = str(s))
textPad.pack()

root.mainloop()