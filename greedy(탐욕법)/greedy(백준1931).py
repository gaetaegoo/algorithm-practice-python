# https://www.acmicpc.net/problem/1931
# 백준 1931 - 회의실 배정

import sys
input = sys.stdin.readline

# 회의의 갯수 지정
n = int(input())
time = []

# 각각의 회의시간을 설정
for i in range(n):
    first, second = map(int, input().split())
    time.append([first, second])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0    # 회의의 마지막 시간을 저장할 변수
count = 0   # 회의 카운트를 저장할 변수

for i, j in time:
    if i >= last:   # 회의 시작 시간이 회의의 마지막 시간보다 크거나 같다면
        count += 1  # 회의 카운트에 1씩 추가
        last = j

print(count)