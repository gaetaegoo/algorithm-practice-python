'''
implementaion(구현) 실전 문제
게임 개발 p.118
'''

import sys

input = sys.stdin.readline

# (입력 조건1) n, m을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵 생성 후 0으로 초기화
d = [[0] * m for _ in range(n)]

# (입력 조건2) 현재 캐릭터의 x좌표, y좌표, 방향을 입력
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# (입력 조건3) 전체 맵 정보를 입력 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향으로 이동할 때 좌표
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 (방향만) 회전(북:0, 동:1, 남:2, 서:3)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1  # 맨 처음 서 있는 좌표를 방문 처리
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 저면에 가보지 않은 칸이 존재할 때 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)

# 방법2 ---------------------------------------------------------------------

import sys

input = sys.stdin.readline

# (입력 조건1)맵 크기 지정
N, M = map(int, input().split())

# (입력 조건2)현재 위치 및 방향 지정
# (북:0, 동:1, 남:2, 서:3)
A, B, d = map(int, input().split())

# 전체 맵 입력(육지:0, 바다:1)
input_map = []
for i in range(N):
    input_map.append(list(map(int, input().split())))

# 이동할 수 있는 모든 경우(북, 동, 남, 서)
move_steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 바라보는 방향의 모든 경우
# (북:0, 동:1, 남:2, 서:3)
d_steps = [0, 1, 2, 3]

# 캐릭터가 회전한 횟수
count = 0

# 캐릭터가 방문가능한 총 지역
result = 0

# 현재 좌표 방문(방문한 곳은 2로 처리함)
input_map[A][B] = 2
result += 1

while True:
    d = d_steps[d - 1]  # -1을 해주면 왼쪽으로 방향 전환

    # 현재 위치값 + 이동할 위치값(디렉션 + 이동 방향)
    next_A = A + move_steps[d][0]
    next_B = B + move_steps[d][1]

    # 만약 이동한 위치가 육지(0)라면
    if input_map[next_A][next_B] == 0:
        # 이동한 위치를 현재 위치값으로 저장하고
        A = next_A
        B = next_B
        input_map[A][B] = 2  # 2를 적어주면서 방문한 곳으로 처리
        result += 1
        count = 0
        # print("d = %d" %d + " - (A, B) = (%d, %d)" % (A, B))
    else:
        count += 1
        # print("d =", d)
        # count = 4 일 때, 네 방향 모두 확인 끝
        if count == 4:
            # 현재 바라보는 방향의 반대편인 뒤쪽으로 이동하기 위해 -2
            next_A = A + move_steps[d - 2][0]
            next_B = B + move_steps[d - 2][1]
            # 이미 가본 곳으로 이동(0은 안 가봤던 육지고, 2는 가봤던 육지)
            if input_map[next_A][next_B] != 1:
                A = next_A
                B = next_B
                count = 0
            # 바다(1)라서 뒤로도 못 가는 경우에 종료
            else:
                break

# print("A, B 위치 = (%d, %d)" % (A, B), end=', ')
# print("result", result, end=', ')
# print("map:", input_map)
print(result)
