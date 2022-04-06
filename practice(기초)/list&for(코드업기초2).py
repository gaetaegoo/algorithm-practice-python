# https://codeup.kr/problem.php?id=6097
# 6097 : [기초-리스트] 설탕과자 뽑기

'''
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
'''

# h: 격자판 세로
# w: 격자판 가로
# n: 막대의 개수
# l: 각 막대의 길이
# d: 막대의 방향(가로는 0, 세로는 1)
# x, y: 막대의 가장 왼쪽 또는 위쪽의 위치

# 격자판의 세로와 가로 길이
h, w = map(int, input().split())

# 세로와 가로 길이에 맞게 격자판 생성
pan = [[0 for j in range(w)] for i in range(h)]

# 막대의 개수
n = int(input())

# 막대의 길이, 방향, 좌표
for i in range(n):
    l, d, x, y = map(int, input().split())

    # 막대의 길이만큼 반복
    for j in range(l):
        if d == 0:      # 막대가 가로(0)라면
            pan[x-1][y-1+j] = 1
        else:           # 막대가 세로(1)라면
            pan[x-1+j][y-1] = 1
    '''
    x, y에서 1씩 뺴주는 이유는
    입력 좌표 x, y가 [0, 0]부터 시작하는 것이 아닌
    [1, 1]부터 시작하기 떄문
    '''

# 막대가 놓인 격자판 출력
for i in range(h):
    for j in range(w):
        print(pan[i][j], end=' ')
    print()

# 겁나 어려운 줄 알았는데 이해하니 쉽네?