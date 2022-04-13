# https://codeup.kr/problem.php?id=2001
# 2001 : 최소 대금

pasta = []
for i in range(3):
    pasta.append(int(input()))

juice = []
for i in range(2):
    juice.append(int(input()))

price = (min(pasta) + min(juice)) * 1.1

# format() 함수를 까먹지 말자
print(format(price, '.1f'))
