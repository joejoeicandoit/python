#################################################
# FTP 서버에서 파일 다운로드 by. yojucho
# pyinstaller [Python file] --onefile --noconsole
#################################################
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from ftplib import FTP
import os
import shutil


# dateBox의 입력값을 8자리로 제한
def _limit_char(int):
    _init_message()
    return len(int) <= 8

## 출력 메세지값 초기화
def _init_message():
    result_label.configure(text="")
    err_label.configure(text="")
    downloadPath.configure(text="")

# dateBox 값 초기화
def _init_dateBox():
    dateBox.delete(0, END)

# 날짜박스에 입력한 값이 int인지 검증
def _isint():
    value = dateBox.get()
    try:
        int(value, 10)
    except ValueError:
        return False
    except TypeError:
        return False
    else:
        return True

# 다운로드로 지정한 폴더내 파일 삭제
def _removeAllFile(filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(file.path)
        else:
            pass

# 다운로드 폴더선택
def _selectDownload_Folder():
    _init_message()
    win.dirName = filedialog.askdirectory()
    dirPath = win.dirName
    _removeAllFile(dirPath)
    return win.dirName
    #downloadPath.configure(text="다운로드 경로： " + win.dirName)
    #downloadPath.configure(text="ダウンロード先： " + win.dirName)

# 0Kb 파일삭제
def _delete_zeroSize_files(dirPath):
    #win.dirName = filedialog.askdirectory()
    #dirPath = win.dirName
    file_list = os.listdir(dirPath)
    for file in file_list:
        file = dirPath + "\\"+ file
        mysize = os.path.getsize(file)

        if mysize <= 0:
            os.remove(file)
        else:
            pass
            #print(file_name + " :" ,mysize)

## 다운로드한 파일의 확장자 변경
def _change_fileExt(dirPath):
    changeExt = "log"
    target = os.listdir(dirPath)
    for i in range(len(target)):
        extension = target[i].find(".")
        convert = target[i][:extension + 1] + changeExt
        os.rename(dirPath + '/'+ target[i], dirPath + '/' + convert)

# FTP 서버 접속해서 파일 다운로드 실행
def _filedown_Stsrt(dirPath):    
    # ------- FTP 서버 정보 -------
    #ftpSvrIp=('127.0.0.1')
    ftpSvrIp=['127.0.0.1', '127.0.0.1']
    user='testuser'
    passwd='testpass'
    sourceDir=['TestWorld', 'OfficeTest']
    # ------- FTP 서버 정보 -------

    # FTP 서버접속
    ftp = FTP(ftpSvrIp[radioValue.get()])
    ftp.login(user, passwd)
    ftp.cwd(sourceDir[radioValue.get()] + '/BACKUP/')

    sourceExt = '*.log.pre' #다운로드할 파일
    fileDate = ""
    logFile = ""
    path = ""

    fileDate = dateBox.get()
    path = dirPath

    logFile = fileDate + sourceExt #'*.log.pre'
    files = ftp.nlst(logFile)
    for file in files:
        with open(path +'\\' + file, 'wb') as f:
            ftp.retrbinary('RETR %s' % file, f.write)

    ftp.quit()
    ## FTP 접속종료


# -----< 다운로드 버튼클릭 >-----
def LogFileDownload_Click():
    checkValue = _isint()
    textbox_len = len(dateBox.get())
    value = dateBox.get()

    # 8자리의 정수가 입력될 경우 실행
    if checkValue == True and textbox_len == 8:
        dirPath = _selectDownload_Folder()
        _filedown_Stsrt(dirPath)
        _init_dateBox()
        _delete_zeroSize_files(dirPath)
        _change_fileExt(dirPath)

        result_label.configure(text="로그파일 (" + value + ") 을 다운로드 했습니다.")
        #result_label.configure(text="Logファイル (" + value + ") をダウンロードしました。")
    else:
        _init_message()
        _init_dateBox()
        err_label.configure(text="올바른 값을 입력해 주세요")
# -----< 다운로드 버튼클릭 >-----


# App 화면구성
win = Tk()
win.title("파일 다운로더")
#win.title("【Title】 LogFile Download")
win.geometry("540x300+100+100")
win.resizable(False, False)

# 주의 문구
alertLbl1 = Label(win, text="주의: 로그 파일이 없는경우에는 하루 전으로 설정해 주세요.")
alertLbl2 = Label(win, text="주의: 다운로드로 지정한 폴더내의 파일은 삭제 됩니다.")
#alertLbl1 = Label(win, text="注意: ログファイルが無い時は日付を1日前にしてみて下さい")
#alertLbl2 = Label(win, text="注意: ダウンロードフォルダの中にある既存ファイルは削除されます")
alertLbl1.place(x=10, y=10)
alertLbl2.place(x=10, y=30)

# 서버 선택용 라디오 버튼
radioValue = IntVar()
radioValue.set(0)
radioOne = Radiobutton(win, text='PUB환경', variable=radioValue, value=0)
radioTwo = Radiobutton(win, text='IBT환경', variable=radioValue, value=1)
radioOne.place(x=10, y=70)
radioTwo.place(x=100, y=70)

# 날자입력용 텍스트 박스
dateLbl1 = Label (win, text="날짜：")
#dateLbl1 = Label (win, text="日付`：")
vc = win.register(_limit_char)
dateBox = ttk.Entry(win, width=8, textvariable=int, validate="key", validatecommand=(vc, "%P"))

# 다운로드 버튼위치
downBtn = Button(win, text="다운로드 시작", command=LogFileDownload_Click)
#downBtn = Button(win, text="ダウンロード開始", command=LogFileDownload_Click)
dateLbl1.place(x=10, y=100)
dateBox.place(x=50, y=100)
downBtn.place(x=120, y=95)

# 다운로드 경로 표시용 메세지
downloadPath = Label(win, text=" ")
downloadPath.place(x=10, y=130)

# 결과 표시용 메세지
result_label = Label(win, foreground = 'blue')
result_label.place(x=10, y=150)

# 에러 표시용 메세지
err_label = Label(win, foreground = 'red')
err_label.place(x=10, y=170)

win.mainloop()
# App 화면구성: