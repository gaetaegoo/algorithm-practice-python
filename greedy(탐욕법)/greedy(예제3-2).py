# 실전 문제 - 큰 수의 법칙
'''
다양한 수로 이루어진 배열이 있을 때
주어진 수들을 M번 더하여 가장 큰 수를 만들어라
단 배열의 특정한 인덱스(번호)에 해당하는 수가
연속해서 K번을 초과하여 더해질 수 없다
'''

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

# 두번 째 방법 ---------------------------------------------------------------

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())     # 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))  # 공백으로 구분하여 리스트에 담기

data.sort() # 입력 받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2]    # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때 마다 1씩 빼기
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)
