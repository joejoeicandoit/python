import tkinter, tkinter.messagebox


def btn_click():
    ftplist=['192.168.0.1', '192.168.1.1']
    num = radioValue.get()

    tkinter.messagebox.showinfo("체크한 항목은?", ftplist[num])

win = tkinter.Tk()
win.geometry("540x300+100+100")
win.resizable(False, False)
win.title("라디오버튼")

# 라디오 버튼: 파일서버 선택
radioValue = tkinter.IntVar()
radioValue.set(0)
radioOne = tkinter.Radiobutton(win, text='PUB환경', variable=radioValue, value=0)
radioTwo = tkinter.Radiobutton(win, text='IBT환경', variable=radioValue, value=1)
radioOne.place(x=10, y=70)
radioTwo.place(x=100, y=70)


btn = tkinter.Button(win, text="값취득", command=btn_click)
btn.place(x=200, y=170)

win.mainloop()