import ftplib
#from ftplib import FTP_TLS
from logging import getLogger, StreamHandler, Formatter, DEBUG



'''
## FTPS (FTP over SSL) 서버에 접속해서 디렉토리내의 파일 취득
try: 
    ftps = FTP_TLS()
    ftps.connect('172.17.100.102', 9900)
    ftps.auth()
    ftps.login('yojucho@gameonidc.idc', 'ebisu202105!#')
    ftps.prot_p()
    ftps.set_pasv(True)
    print("FTPに接続しました")
    
    dst_path = "/Teams/PCContents/Personal/yojucho/uploadtest/"    
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

##
try:
    #filename = "ftp_logger.log"
    filename = "itemPackageCustomDataClient.dat"
    #with open(filename, 'rb') as f:
        #ftps.storbinary('STOR ' + filename, f)
    with open(filename, 'wb') as f:
        ftps.retrbinary('RETR ' + filename, f.write)
except Exception as e:
    print("例外が発生しました: ", e)


#ftps.quit()
#ftps.close()
#print("Upload OK")

#for fname in scr_path:
#        print('Uploding: ', fname)
#with open(scr_path, 'rb') as fb:
#    ftps.storbinary('STOR '+ dst_path, fb.write) #바이너리 전송 모드로 파일을 저장한다.
'''

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
        
        ftps.connect('172.17.100.102', 9900)
        ftps.auth()
        ftps.login('yojucho@gameonidc.idc', 'ebisu202108!#')
        ftps.set_debuglevel(2)
        ftps.prot_p()
        ftps.set_pasv(True)
        #print("FTPに接続しました")

        dst_path = "/Teams/PCContents/Personal/yojucho/uploadtest"
        ftps.cwd(dst_path)  # FTP서버 지정 디렉토리 이동
        #ftplib._SSLSocket = None
        
        ''' 
        1.ftps.connect('172.17.100.102', 9900, timeout=60)
         FTP서버로 파일 업로드 하고, 일정시간 프리즈 상태로 있다 업로드한 파일 삭제후 에러
         timeout 60초를 설정 하면 업로드 가능하고, 그 외 시간은 에러
         파일 업로드 완료 까지 항상 1분을 기다려야 하는 문제 발생

        2.ftplib._SSLSocket = None
         timeout 설정 없이 파일 업로드가 완료 되면 바로 접속을 종료

        '''

        file_name = 'japan.llt'
        with open(file_name, 'rb') as f:
            ftps.storbinary('STOR ' + file_name, f, callback=None, rest=None)
            #ftps.storlines('STOR ' + file_name, f)


        #ftps.close()

    except ftplib.all_errors as e:
            logger.error('FTP error = %s' % e)
    else:
            logger.debug('FTP Succes???')
logger.debug('=== End FTP ===')





''''
    os.chdir('C:/temp')
    files = glob.glob('*.*')    
    #files = glob.glob(r'C:\temp\*.*')
    for filename in files:
        print('file: ' + filename)
        with open(filename, 'rb') as f:
            ftps.storbinary('STOR' + filename, f)

except Exception as e:
    print("Error が発生しました：", e)


def ftpDownload(scr_path, dst_path):
    from ftplib import FTP_TLS
    import os

    ftps = FTP_TLS()
    ftps.connect('172.17.100.102', 9900)
    ftps.auth()
    ftps.login('yojucho@gameonidc.idc', 'ebisu202105!#')
    ftps.prot_p()
    ftps.set_pasv(True)

    ftps.cwd(dst_path)

    files = ftps.nlst('*.dat')

    for fname in files:
        print('Downloading: ', fname)
        with open(fname, 'wb') as f:
            ftps.retrbinary('RETR ' + fname, f.write) #바이너리 전송 모드로 파일을 가져온다
        
    print("Download OK")
    ftps.quit()
'''
