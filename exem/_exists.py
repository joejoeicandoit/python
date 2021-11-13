import glob

files = glob.glob("C:/temp/AUtempR/*")

if len(files) <= 0:
    print("ファイルがありません")
else:
    print("ファイルがあります")



#for file in files:
#   print(file)