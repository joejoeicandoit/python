# Flaskを使ってシンプルなブログを構築する

## flask 起動(power shell)
 > $env:FLASK_APP = "app"   ← filename of python
 > $env:FLASK_ENV = "development"   ← debugmode
 > flask run

### Part1
 - サーバーを立ち上げる  
 - 変数を利用する  
 - htmlファイルを読み込んで表示させる  
 - formでデータを渡す  
 - for文、if文を取り込んでコードをシンプルに作成する  
  
### Part2
 - 要素の共通化（Jinja2 Template）  
 - Database作成（SQLite3）  
 - 表示、新規作成、編集、削除の機能を取り込む  
  
### Part3
 URL https://youtu.be/Gyy1tzwenc8
 - サインアップ&ログイン機能を実装
     3-1. Flask-Login Install (https://flask-login.readthedocs.io/en/latest/)  
     3-2. ユーザDBの作成
 - CSSの適用
 - Bootstrapの適用
   - > pip3 install flask-bootstrap