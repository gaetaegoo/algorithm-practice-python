# https://codeup.kr/problem.php?id=6098
# 6098 : [기초-리스트] 성실한 개미

'''
(방법 1) 빈 미로판을 0으로 채운 후, for문 돌면서 채워 넣기
miro = [[0 for j in range(10)] for i in range(10)]

for i in range(10):
    miro[i] = list(map(int, input().split()))
'''

# (방법 2) 빈 리스트 생성 후, append로 바로 채워 넣기
# 이게 더 직관적이고 좋은 듯?
miro = []
for i in range(10):
    miro.append(list(map(int, input().split())))

# 개미집 위치 설정(start하는 곳)
x, y = 1, 1

# 개미 이동 경로 로직
# 방문처리 -> 종료조건 -> 이동
while True:
    if miro[x][y] == 0:    # 방문하지 않은 곳이면
        miro[x][y] = 9     # 9로 방문 처리
    elif miro[x][y] == 2:  # 먹이(2)에 도착했다면 break
        miro[x][y] = 9
        break

    # 전진(y+1)해도 1이고, 우회전(x+1)해도 1이면 break
    if miro[x][y+1] == 1 and miro[x+1][y] == 1:
        break

    if miro[x][y+1] != 1:   # 전진 했을 때 1이 아니라면(막힌 곳) 전진
        y += 1
    elif miro[x+1][y] != 1: # 우회전 했을 때 1이 아니라면(막힌 곳) 우회전
        x += 1

# 최종 이동한 경로 출력
for i in range(10):
    for j in range(10):
        print(miro[i][j], end=' ')
    print()

# while까지는 생각을 해냈는데, 그 이후에 너무 어렵게 생각해서 꼬여 버렸던 문제
