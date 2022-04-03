# https://www.acmicpc.net/problem/11399
# 백준 1931 - ATM

import sys
input = sys.stdin.readline

N = int(input())
Pi = list(map(int, input().split()))
Pi.sort()   # 걸리는 시간을 오름차순으로 정리

time = 0    # 각 사람마다 걸리는 시간
sum = 0     # 걸리는 총 시간

for i in Pi:        # 각 시간을 돌면서 반복
    time += i       # 각 사람마다 걸리는 시간을
    sum += time     # 반복문을 돌면서 sum에 합침

print(sum)