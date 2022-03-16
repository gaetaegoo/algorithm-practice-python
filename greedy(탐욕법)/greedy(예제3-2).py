# 실전 문제 - 큰 수의 법칙

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())     # 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))  # 공백으로 구분하여 리스트에 담기

data.sort() # 입력 받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2]    # 두 번째로 큰 수

count = int(m / (k + 1)) * k    # 가장 큰 수가 더해지는 횟수 계산
count += m % (k + 1)    # 나머지 만큼 큰 수를 더하는 횟수 증가

result = 0
result += (count) * data[n - 1] # 가장 큰 수 더하기
result += (m - count) * data [n - 2]    # 두 번째로 큰 수 더하기

print(result)

