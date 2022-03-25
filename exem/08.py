# Q8 역순 저장
# 다음과 같은 내용의 파일 abc.txt가 있다.
# AAA
# BBB
# CCC
# DDD
# EEE
#
# 이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.
# EEE
# DDD
# CCC
# BBB
# AAA


f = open("C:\\Users\\yojucho\\OneDrive\\_Source\\_Python\\exem\\abc.txt", 'r')
# f = open(".\abc.txt", 'r')
text = f.readlines()
f.close()

print(text)

text.reverse()

print("Type: ", type(text))


f = open("C:\\Users\\yojucho\\OneDrive\\_Source\\_Python\\exem\\abc2.txt", 'w')
i = 0
for line in text:
    line = line.split()    
    #print(line)
    
    f.write(line)
    f.write('\n')
f.close()
