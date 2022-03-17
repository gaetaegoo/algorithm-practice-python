# https://www.acmicpc.net/problem/11047
# 백준 11047 - 동전 0

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
Ai = [] # 동전의 가치를 저장할 빈 리스트
count = 0   # 필요한 동전의 총 개수

'''
동전의 가치 리스트의 인덱스 변수
문제에서 동전의 가치 리스트는 오름차순으로 주어진다고 하였으니 
가장 큰 값은 배열의 맨뒤에 저장되어 N-1을 저장한다.
'''
i = n - 1

for _ in range(n):  # 동전의 종류 수 만큼 반복
    Ai.append(int(input())) # 위에서 선언한 빈 리스트에 10종류의 동전 담기

while k != 0:   # k가 0이 될 때까지 반복
    count += k // Ai[i] # 동전의 개수를 저장(몫 만큼 카운트)
    k %= Ai[i]  # 동전의 가치로 나눈 나머지를 저장
    i -= 1  # 인덱스 감소(동전의 크기가 점점 작아지며 대조)

print(count)

# 두 번째 방법 --------------------------------------------------

# 1. 계산대 안에 있는 돈의 수와 거슬러 줄 돈을 구함
N, K = map(int, input().split())    # N: 화폐 종류수, K: 거슬러 줄 돈

# 2. 계산대에 있는 화폐들을 리스트의 형태로 입력 받음
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
# coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

# 3. 만약 '계산대 안에 있는 화폐'보다 '거슬러 줄 돈'이 크다면 돈을 거슬러 줌
answer = 0
for coin in coins:
    if K >= coin:
        answer += K // coin #몫만큼 더하기
        K %= coin   #나머지 할당
        if K <= 0: # 만약 K가 0이면 반복문을 탈출합니다.
            break
print(answer) # 거슬러 준 동전 + 화폐의 수