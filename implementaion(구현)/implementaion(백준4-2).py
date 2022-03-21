# 대표적인 implementaion(구현) 문제
# 시각 - p.113

import sys
input = sys.stdin.readline

n = int(input())

count = 0

# 전체 시, 분, 초에 대한 경우의 수 = 24 X 60 X 60 == 86,400
# 3중 반복문으로 완전하게 탐색
for i in range(n + 1):      # 0~n시(입력 받은 시)까지 검사
    for j in range(60):     # 0~59분까지 검사
        for k in range(60): # 0~59초까지 검사
            # 모든 경우의 수에서 3이 들어간 경우를 검사
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)