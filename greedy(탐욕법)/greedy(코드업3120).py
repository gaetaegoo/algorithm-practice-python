# https://codeup.kr/problem.php?id=3120
# 3120 : 리모컨

a, b = map(int, input().split())
target = abs(a-b)   # 절대값 함수
sum = 0             # 온도 조절 횟수

while target != 0:
    if target >= 8:
        target = abs(target - 10)
        sum += 1
    elif 8 > target >= 3:
        target = abs(target - 5)
        sum += 1
    elif 3 > target >= 1:
        target = abs(target -1)
        sum += 1

print(sum)

# 몫과 나머지를 활용한 방법(시간초과 뜨긴 함) -------------------
a, b = map(int, input().split())
target = abs(a-b)
sum = target // 10     # 미리 10으로 나눈 몫을 sum에 추가

while target != 0:
    if target % 10 in [1, 5]:   # 나머지가 1, 5라면 1 추가
        sum += 1
    elif target % 10 in [2, 4, 6, 9]: # 나머지가 2, 4, 6, 8이라면 2 추가
        sum += 2
    elif target % 10 in [3, 7, 8]:  # 나머지가 3, 7, 8이라면 3 추가
        sum += 3

print(sum)
