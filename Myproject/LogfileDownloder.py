# FTPサーバから特定ファイルのダウンロード
# pyinstaller [Python file] --onefile --noconsole
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ftplib import FTP
import os
import shutil

logpre = '*.log.pre'
changeLog = "log"

# ファイルダウンロードボタン
def LogFileDownload_Click():
    _vaildate_textbox()

# TextBoxの中身チェック
def _vaildate_textbox():
    value = textbox.get()    
    textbox_len = len(textbox.get())
    num = 8

    if value is "":
        err_label.configure(text="日付を入力してください")

    elif num > textbox_len:
        err_label.configure(text="日付を確認して下さい (ex 20200101)")

    elif num < textbox_len:
        err_label.configure(text="正しい日付を入力してください：" + value)
        textBox_Clear()

    else:        
        _selectDownload_Folder()
        _filedown_Stsrt(logpre, changeLog)        
        result_label.configure(text="Logファイル (" + value + ") をダウンロードしました。")
        textBox_Clear()

# ファイルダウンロード先
def _selectDownload_Folder():    
    err_label.configure(text="")
    downloadPath.configure(text="")
    win.dirName = filedialog.askdirectory()
    downloadPath.configure(text="ダウンロード先： " + win.dirName)      

# ダウンロードフォルダ内のファイル削除
def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):            
            os.remove(file.path)
        else:
            pass


# ダウンロード実施
def _filedown_Stsrt(logpre, changeLog):
    # FTP接続
    ftp = FTP('xxx.xxx.xxx.xxx')
    ftp.login('USER','PADDWORD')
    ftp.cwd('TestWorld/BACKUP/')
    
    fileDate = ""
    logFile = ""
    path = ""

    fileDate = textbox.get()
    path = win.dirName       
    
    
    removeAllFile(path)

    logFile = fileDate + logpre #'*.log.pre'
    files = ftp.nlst(logFile)
    for file in files:
        with open(path +'\\' + file, 'wb') as f:
            ftp.retrbinary('RETR %s' % file, f.write)

    # Delete 0Kb Files
    file_list = os.listdir(path)   
    for file in file_list:
        #file_name = file      
        file = path + "\\"+ file
        mysize = os.path.getsize(file)

        if mysize <= 0:
            os.remove(file)
        else:
            pass
            #print(file_name + " :" ,mysize)

    ## Files 拡張子変更
    #changeLog = "log"
    target = os.listdir(path)
    for i in range(len(target)):
        extension = target[i].find(".")
        convert = target[i][:extension + 1] + changeLog
        os.rename(path + '/'+ target[i], path + '/' + convert)

    ## FTP接続終了
    ftp.quit()
    textBox_Clear()

# textbox削除        
def textBox_Clear():
    textbox.delete(0, END)

### 画面構成 ###
win = Tk()
win.title("【Title】 LogFile Download")
win.geometry("540x300+100+100")
win.resizable(False, False)
#
lbl1 = Label(win, text="注意: ログファイルが無い時は日付を1日前にしてみて下さい")
#lbl1.pack()
lbl1.place(x=10, y=10)

lbl3 = Label(win, text="注意: ダウンロードフォルダの中にある既存ファイルは削除されます")
lbl3.place(x=10, y=30)

lbl2 = Label (win, text="日付：")
lbl2.place(x=10, y=100)

textbox = ttk.Entry(win, width=8, textvariable=str)
textbox.place(x=50, y=100)

btn1 = Button(win, text="LogFileDownload", command=LogFileDownload_Click)
btn1.place(x=120, y=95)

downloadPath = Label(win, text=" ")
downloadPath.place(x=10, y=130)

result_label = Label(win, foreground = 'blue')
result_label.place(x=10, y=150)

err_label = Label(win, foreground = 'red')
err_label.place(x=10, y=170)

### 画面表示 ###
win.mainloop()
