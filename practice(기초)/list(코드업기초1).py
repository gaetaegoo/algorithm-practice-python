# https://codeup.kr/problem.php?id=6095
# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기

'''
[입력]
바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력된다.
n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 똑같은 좌표는 입력되지 않는다.

[출력]
흰 돌이 올려진 바둑판의 상황을 출력한다.
흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력한다.
'''

# 흰 돌을 놓을 횟수
n = int(input())

# 19 x 19 바둑판 생성
d = [[0 for j in range(20)] for i in range(20)]

# 흰 돌이 놓인 좌표는 1로 표시(검은 돌은 0)
for i in range(n):
    x, y = list(map(int, input().split()))
    if d[x][y] == 1:            # (예외처리) 만약 돌이 이미 놓여 있다면 continue
        continue
    d[x][y] += 1

# 전체 좌표 출력
for i in range(1, 20):          # i(row(행))을 돌면서
    for j in range(1, 20):      # j(column(열))를 돌면서
        print(d[i][j], end=' ') # 각 좌표에 맞는 인덱스 값을 출력(띄어쓰기 하면서)
    print()                     # 한 row(행)가 끝날 때 마다 줄 바꾸기
