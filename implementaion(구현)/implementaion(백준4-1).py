# 대표적인 implementaion(구현) 문제
# 상하좌우 - p.112

import sys
input = sys.stdin.readline

n = int(input())        # 지도 크기
plans = input().split() # 움직일 경로

x, y = 1, 1 # 초기 위치 지정

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 움직일 경로를 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나면 무시하고 for문으로(continue)
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

# 더 간단히 푸는 방법(딕셔너리 활용) ---------------------

n = int(input())
plans = input().split()

# 딕셔너리에 미리 L, R, U, D 위치값을 지정해준다
directions = {'L':(0, -1), 'R':(0, 1), 'U':(-1, 0), 'D':(1, 0)}
x, y = 1, 1

for plan in plans:
    # 디렉션에 맞는 위치값을 바로바로 대입해준다
    x_plan, y_plan = directions[plan]
    # 기존 위치값 + 디렉션의 위치값
    x_new = x + x_plan
    y_new = y + y_plan
    if x_new < 1 or x_new > n or y_new < 1 or y_new > n:
        continue
    x, y = x_new, y_new

print(x, y)
