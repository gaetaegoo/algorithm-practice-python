# 숫자 카드 게임
'''
여러 개의 숫자 카드 중에서 가장 높은 숫자 카드가 쓰인 카드 한 장을 뽑아라
N은 행이며, M은 열의 개수를 의미
먼저 뽑고자 하는 행을 선택한 후, 그 행에서 가장 낮은 숫자 카드를 뽑는다
행마다 반복 한 후, 가장 낮은 숫자 중에서 -> 가장 높은 숫자 카드를 뽑아라
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)   # 현재 줄에서 '가장 작은 수' 찾기
    result = max(result, min_value) # '가장 작은 수'들 중에서 가장 큰 수 찾기

print(result)