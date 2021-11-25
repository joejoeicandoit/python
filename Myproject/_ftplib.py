#############################################################
# FTP_TLS 서버로 파일 업로드 하기 by. yojucho
# pyinstaller 파일이름.py --onefile --noconsole
# >>> 작업중 <<<
#############################################################
import ftplib
#from ftplib import FTP_TLS
from logging import getLogger, StreamHandler, Formatter, DEBUG


# 로그 출력 설정
logger = getLogger("FTP Test")
logger.setLevel(DEBUG)
stream_handler = StreamHandler()
stream_handler.setLevel(DEBUG)
formmater = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formmater)
logger.addHandler(stream_handler)

logger.debug('=== Start FTP ===')
with ftplib.FTP_TLS() as ftps:
    try:
        
        ftps.connect('FTP 서버IP', 9900)
        ftps.auth()
        ftps.login('유저 어카운트', '유저 패스워드')
        ftps.set_debuglevel(2)
        ftps.prot_p()
        ftps.set_pasv(True)
        #print("FTPに接続しました")

        dst_path = "/업로드위치"
        ftps.cwd(dst_path)  # FTP서버 지정 디렉토리 이동
        #ftplib._SSLSocket = None
        
        ''' 
        # FTP서버로 파일을 업로드 한 후 일정시간 프리즈 상태로 있다가 에러, 업로드 된 파일을 삭제

        1. ftps.connect('FTP 서버IP', 9900, timeout=60)
         timeout 60초를 설정 하면 업로드 가능, 그 외 시간은 에러
         파일 업로드 완료 까지 항상 1분을 기다려야 하는 문제 발생

        2. ftplib._SSLSocket = None
         해당 코드를 추가
         timeout 설정 없이 파일 업로드가 완료 되면 바로 접속 종료
        '''

        file_name = 'japan.llt'
        with open(file_name, 'rb') as f:
            ftps.storbinary('STOR ' + file_name, f, callback=None, rest=None) #바이너리 모드로 업로드
            #ftps.storlines('STOR ' + file_name, f)


        #ftps.close()

    except ftplib.all_errors as e:
            logger.error('FTP error = %s' % e)
    else:
            logger.debug('FTP Succes???')
logger.debug('=== End FTP ===')




'''
## FTPS (FTP over SSL) 서버의 디렉토리에 있는 파일 취득
try: 
    ftps = FTP_TLS()
    ftps.connect('FTP 서버IP', 9900)
    ftps.auth()
    ftps.login('유저 어카운트', '유저 패스워드')
    ftps.prot_p()
    ftps.set_pasv(True)
    print("FTPに接続しました")
    
    dst_path = "/업로드위치"
    ftps.cwd(dst_path) #FTP서버 디렉토리 이동
    files = ftps.nlst("*.*") #파일취득
    for filename in files:
        print("Filename: " + filename)

    ftps.quit()
except Exception as e:
    print("FTPに接続出来ませんでした: ", e)


## 디렉토리 내의 파일 취득(Windows)
try:
    
    #os.chdir("C:/temp/")
    files = glob.glob(r'C:\temp\*.*')

    for filename in files:
        print("Filename: " + filename)
except Exception as e:
    print("Error が発生しました：", e)



## FTP 파일 다운로드
def ftpDownload(scr_path, dst_path):
    from ftplib import FTP_TLS
    import os

    ftps = FTP_TLS()
    ftps.connect('FTP 서버IP', 9900)
    ftps.auth()
    ftps.login('유저 어카운트', '유저 패스워드')
    ftps.prot_p()
    ftps.set_pasv(True)

    ftps.cwd(dst_path)

    files = ftps.nlst('*.dat')

    for fname in files:
        print('Downloading: ', fname)
        with open(fname, 'wb') as f:
            ftps.retrbinary('RETR ' + fname, f.write) #바이너리 전송 모드로 다운로드
        
    print("Download OK")
    ftps.quit()
'''