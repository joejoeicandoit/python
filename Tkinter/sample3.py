from tkinter import *


window = Tk()
choice = IntVar()

def clickUpload():
    result = 'Upload を完了しました。'
    label.configure(window, text='結果：' + result)


Label(window, text='What files do you Upload?', justify = LEFT, padx = 20).pack()

Radiobutton(window, text='Itemdata Files', padx = 20, variable = choice, value = 1).pack(anchor=W)
Radiobutton(window, text='Textdata Files', padx = 20, variable = choice, value = 2).pack(anchor=W)

Button(window, text='Upload', command=clickUpload).pack()
Button(window, text='Close', command=window.destroy).pack()

label = Label(window, text='結果：')
label.pack(anchor=W)

window.mainloop()