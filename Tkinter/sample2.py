from tkinter import *
from math import *

def calculate(event):
    result = eval(entry.get()) # entry 에서 가져온 문자열 내용대로 계산한다.
    label.configure(text = '結果 : ' + str(result)) # 생성한 라벨에 결과값을 붙인다.
    


# UI 정의 #
window = Tk()

Label(window, text='Python 計算機').pack()

entry = Entry(window)
entry.bind('<Return>', calculate) # entry에 엔터를 누르면 calculate 함수가 호출된다.
entry.pack()

label = Label(window, text = '結果 : ') # 라벨생성
label.pack()

window.mainloop()