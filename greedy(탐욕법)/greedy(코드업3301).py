# https://codeup.kr/problem.php?id=3301
# 3301 : 거스름돈

# 방법 1 ----------------------------------------------
n = int(input())

num = 0
change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in change:    # if절과 break 활용
    if n >= i:
        num += n // i
        n %= i
        if n <= 0:
            break

print(num)

# 방법 2 ----------------------------------------------
n = int(input())

num = 0
change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in change:    # 단순히 for문만 돌려도 됨
    num += n // i
    n = n % i

print(num)
