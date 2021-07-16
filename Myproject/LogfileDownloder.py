#################################################
# FTP 서버에서 파일 다운로드 by. yojucho
# pyinstaller [Python file] --onefile --noconsole
#################################################
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ftplib import FTP
import os
import shutil

# 다운로드할 파일의 확장자 설정
logpre = '*.log.pre'
changeLog = "log"


# 다운로드 버튼 클릭
def LogFileDownload_Click():
    _vaildate_textbox()

# dateBox에 입력한 날짜값 체크
def _vaildate_textbox():
    value = dateBox.get()    
    textbox_len = len(dateBox.get())
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

# 파일 다운로드 경로
def _selectDownload_Folder():    
    err_label.configure(text="")
    downloadPath.configure(text="")
    win.dirName = filedialog.askdirectory()
    downloadPath.configure(text="ダウンロード先： " + win.dirName)      

# 다운로드로 지정한 폴더내 파일 삭제
def removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):            
            os.remove(file.path)
        else:
            pass


# 다운로드 실행
def _filedown_Stsrt(logpre, changeLog):
    # ------- FTP 접속 정보 -------
    ftp = FTP('xxx.xxx.xxx.xxx')
    ftp.login('USER','PADDWORD')
    ftp.cwd('TestWorld/BACKUP/')
    # ------- FTP 접속 정보 -------
    
    fileDate = ""
    logFile = ""
    path = ""

    fileDate = dateBox.get()
    path = win.dirName       
    
    
    removeAllFile(path)

    logFile = fileDate + logpre #'*.log.pre'
    files = ftp.nlst(logFile)
    for file in files:
        with open(path +'\\' + file, 'wb') as f:
            ftp.retrbinary('RETR %s' % file, f.write)

    # 파일 사이즈 0Kb 삭제
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

    ## 파일 확장자 변경
    #changeLog = "log"
    target = os.listdir(path)
    for i in range(len(target)):
        extension = target[i].find(".")
        convert = target[i][:extension + 1] + changeLog
        os.rename(path + '/'+ target[i], path + '/' + convert)

    ## FTP 접속종료
    ftp.quit()
    textBox_Clear()

# dateBox 값 삭제
def textBox_Clear():
    dateBox.delete(0, END)



# App 화면구성: ------------------------- Start ------------------------- 
win = Tk()
win.title("파일 다운로더")
#win.title("【Title】 LogFile Download")
win.geometry("540x300+100+100")
win.resizable(False, False)


# 주의 문구 설정
alertLbl1 = Label(win, text="주의: 로그 파일이 없는경우에는 하루 전으로 설정해 주세요.")
alertLbl2 = Label(win, text="주의: 다운로드로 지정한 폴더내의 파일은 삭제 됩니다.")
#alertLbl1 = Label(win, text="注意: ログファイルが無い時は日付を1日前にしてみて下さい")
#alertLbl2 = Label(win, text="注意: ダウンロードフォルダの中にある既存ファイルは削除されます")
alertLbl1.place(x=10, y=10)
alertLbl2.place(x=10, y=30)

# 라디오 버튼 설정: 로그 파일이 있는 서버선택
radioValue = IntVar()
radioOne = Radiobutton(win, text='PUB환경', variable=radioValue, value=1)
radioTwo = Radiobutton(win, text='IBT환경', variable=radioValue, value=2)
radioOne.place(x=10, y=70)
radioTwo.place(x=100, y=70)

# 텍스트 박스 설정: 날짜값 입력
dateLbl1 = Label (win, text="날짜：")
#dateLbl1 = Label (win, text="日付`：")
dateBox = ttk.Entry(win, width=8, textvariable=str)
downBtn = Button(win, text="다운로드 시작", command=LogFileDownload_Click)
#downBtn = Button(win, text="ダウンロード開始", command=LogFileDownload_Click)
dateLbl1.place(x=10, y=100)
dateBox.place(x=50, y=100)
downBtn.place(x=120, y=95)

# 다운로드 경로 선택
downloadPath = Label(win, text=" ")
downloadPath.place(x=10, y=130)

# 결과 문구 표시
result_label = Label(win, foreground = 'blue')
result_label.place(x=10, y=150)

# 에러 문구 표시
err_label = Label(win, foreground = 'red')
err_label.place(x=10, y=170)


win.mainloop()
# App 화면구성: ------------------------- End ------------------------- 