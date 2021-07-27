import paramiko

# 업로드할 파일
files = ''

# SFTP 접속설정
sftp_config = {
    'host' : 'example.com',
    'port' : '22',
    'user' : 'user',
    'pass' : 'pass'
}

# SSH 접속준비
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(
    sftp_config['host'],
    port=sftp_config['port'],
    username=sftp_config['user'],
    password=sftp_config['pass'])

#SFTP 세션 개시
sftp_connection = client.open_sftp()

#파일 업로드 경로(풀 패스)
connect_path = 'xxx'


for f in files:
    sftp_connection.put(f, connect_path + f)
    sftp_connection.close()

#서버에서 파일 다운로드
#sftp_connection.get(CONNECT_PATH + 'test.csv', 'download_test.csv')


client.close()
