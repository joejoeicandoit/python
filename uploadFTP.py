import ftplib
import logging

def ftp_upload(hostname, username, password, port, upload_src_path, upload_dst_path, timeout):
    logger.info({
        'action': 'ftp_upload',
        'status': 'run'
    })

    # FTP接続 / アップロード
    with ftplib.FTP() as ftp:
        try:
            ftp.connect(host=hostname, port=port, timeout=timeout)
            #パッシブモード設定
            ftp.set_pasv("true")
            #FTPサーバーログイン
            ftp.login(username, password)
            with open(upload_src_path, 'rb') as fp:
                ftp.storbinary(upload_dst_path, fp)

        except ftplib.all_errors as e:
            logger.error({
                'action': 'ftp_upload',
                'message': 'FTP error = %s' % e
            })


# logの設定
logger = logging.getLogger(__name__)
formatter = '%(asctime)s:%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(
    filename='./ftp_logger.log',
    level=logging.DEBUG,
    format=formatter
)
logger.setLevel(logging.INFO)


hostname = 'FTPサーバーIP'  # 接続先サーバーのホスト名
username = 'username'  # ユーザ名
password = 'password'  # ログインパスワード
port = 21  # FTPサーバーのポート
upload_src_path = 'D:/test,txt'  # アップロードするファイルパス
upload_dst_path = 'STOR /test.txt'  # アップロード先のパス(STOR はアップロードする為のFTPコマンドなので必須)
timeout = 50

logger.info("===START FTP===")
ftp_upload(hostname, username, password, port, upload_src_path, upload_dst_path, timeout)
logger.info("===FINISH FTP===")
