from tkinter import *

def show():
    print('名前： %s \n年齢： %s' %(e1.get(), e2.get()))

window = Tk()

Label(window, text='名前').grid(row=0)
Label(window, text='年齢').grid(row=1)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window, text='表示', command=show).grid(row=3, column=1, sticky=W, pady=4)
Button(window, text='終了', command=window.destroy).grid(row=3, column=0, sticky=W, pady=4)

window.mainloop()