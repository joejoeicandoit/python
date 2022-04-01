# Flaskを使ってシンプルなブログを構築する


## Run Flask

### ----- Bash -----
 > $ export FLASK_APP=app  ← filename of python
 > $ export FLASK_ENV=development
 > $ flask run

### ----- PowerShell -----
 > $env:FLASK_APP = "app"   ← filename of python
 > $env:FLASK_ENV = "development"   ← debugmode
 > flask run

##### history
 - ※참조 https://youtu.be/Gyy1tzwenc8
 - 서버 기동, 변수 이용, html 파일 로드, form 으로 데이터 전송  
 - for, if 를 사용해서 코드를 심플하게
 - 요소의 공통화를 실현（Jinja2 Template）  
 - Database 작성（SQLite3）  
 - 블로그의 표시, 신규작성, 편집, 삭제 기능 추가
 - 등록한 유저로 로그인 / 로그아웃 기능 추가
 - CSS 기능 추가
 - Bootstrap 추가
 - 로그인 상태가 아닐 경우 로그인 페이지로 이동
  
 - 아이디 / 비밀번호 미 입력후 로그인 버튼 클릭 : AttributeError > 확인중
   https://de-milestones.com/%E3%80%90python-flask%E3%80%91typeerror-object-has-no-attribute-is_active/
