data = input("숫자를 입력해 주세요: ")
numbers = list(data.split(","))
result = 0

for num in numbers:
    result = result + int(num)

print(result)