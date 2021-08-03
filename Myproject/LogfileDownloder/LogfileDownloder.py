#############################################################
# FTP 서버에서 파일 다운로드 by. yojucho
# pyinstaller LogfileDownloder.py --onefile --noconsole
#############################################################
import os, glob
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as messagebox
from ftplib import FTP


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
    _removeAllFile(win.dirName)
    return win.dirName

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
    ftpSvrIp=['127.0.0.1', '127.0.0.1']
    user='logtools'
    passwd='wkddnjsakstp1!'
    # ------- FTP 서버 정보 -------

    # FTP 서버접속
    ftp = FTP(ftpSvrIp[radioValue.get()])
    ftp.login(user, passwd)
    sourceDir=['TestWorld', 'OfficeTest']
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

# 다운로드된 파일 존제체크
def _check_Folder(dirPath, dateValue):
    files = glob.glob(dirPath + "/*")
    
    if len(files) <= 0:
        messagebox.showwarning("警告", "入力した日付 (" + dateValue + ") のログファイルが存在しません。"
         + "\n" + "1日前に試してみるか、正確な日付の確認をお願いします。")
        #messagebox.showwarning("경고", "해당 날짜의 (" + dateValue + ") 로그파일이 존재하지않습니다."
         #+ "\n" + "하루 전의 날짜로 입력해보세요 ")
    else:
        downloadPath.configure(justify=LEFT, text=" ダウンロード場所： " + "\n" + win.dirName)
        result_label.configure(justify=LEFT, text=" ログファイル (" + dateValue + ") をダウンロードしました。")
        #downloadPath.configure(justify=LEFT, text="다운로드 경로： " + "\n" + win.dirName)
        #result_label.configure(justify=LEFT, text="로그파일 (" + dateValue + ") 을 다운로드 했습니다.")


# -----< 다운로드 버튼클릭 >-----
def download_Click():
    dateValue = dateBox.get()
    checkValue = _isint()
    textbox_len = len(dateBox.get())

    # 8자리의 정수가 입력될 경우 실행
    if checkValue == True and textbox_len == 8:
        dirPath = _selectDownload_Folder()
        _filedown_Stsrt(dirPath)
        _delete_zeroSize_files(dirPath)
        _change_fileExt(dirPath)
        _init_dateBox()
        _check_Folder(dirPath, dateValue)
    else:
        _init_message()
        _init_dateBox()
        messagebox.showerror("警告", "正しい日付 (" + dateValue + ") を入力してください。")
        #messagebox.showerror("경고", "올바른 날짜를 (" + dateValue + ") 입력해 주세요")
# -----< 다운로드 버튼클릭 >-----


# App 화면구성:START
win = Tk()
win.title("파일 다운로더")
win.geometry("540x300+100+100")
win.resizable(False, False)

# 배경이미지 삽입
sourcePath= os.path.dirname( os.path.abspath( __file__ ) ) # python 파일의 절대경로 확인
isfile = os.path.isfile(sourcePath + r"\image\backimg.png")
if isfile == True:
    #print("Image True")
    canvas = Canvas(bg="white",width=240, height=240)
    backImage = PhotoImage(file=sourcePath + r"\image\backimg.png") # 이미지 파일경로 설정
    canvas.place(x=280, y=50)
    canvas.create_image(0, 0, image=backImage, anchor=NW)
else:
    #print("Image False")
    pass


# 주의 문구
alertLbl1 = Label(win, foreground = 'red', text=" ダウンロード場所に指定したフォルダーにファイルがあれば【削除】されます")
#alertLbl1 = Label(win, text="주의: 다운로드로 지정한 폴더내의 파일은 삭제 됩니다.")
alertLbl1.place(x=10, y=10)

# 서버 선택용 라디오 버튼
radioValue = IntVar()
radioValue.set(0)
radioOne = Radiobutton(win, text='PUB(公開環境)', variable=radioValue, value=0)
radioTwo = Radiobutton(win, text='IBT(社内環境)', variable=radioValue, value=1)
#radioOne = Radiobutton(win, text='PUB환경', variable=radioValue, value=0)
#radioTwo = Radiobutton(win, text='IBT환경', variable=radioValue, value=1)
radioOne.place(x=10, y=60)
radioTwo.place(x=110, y=60)

# 날자입력용 텍스트 박스
dateLbl1 = Label (win, text="日付：")
#dateLbl1 = Label (win, text="날짜：")
dateLbl1.place(x=10, y=100)
vc = win.register(_limit_char)
dateBox = Entry(win, width=8, textvariable=int, validate="key", validatecommand=(vc, "%P"))
dateBox.place(x=50, y=100)
downBtn = Button(win, text="ダウンロード開始", command=download_Click)
#downBtn = Button(win, text="다운로드 시작", command=download_Click)
downBtn.place(x=120, y=95)

dateLbl2 = Label(win, text="(日付は半角数字で入力してください (20210721))")
dateLbl2.place(x=10, y=125)


# 다운로드 경로 표시용 메세지
downloadPath = Label(win, text=" ")
downloadPath.place(x=10, y=150)

# 결과 표시용 메세지
result_label = Label(win, foreground = 'blue')
result_label.place(x=10, y=200)

# 에러 표시용 메세지
err_label = Label(win, foreground = 'red')
err_label.place(x=10, y=200)

win.mainloop()
# App 화면구성:END