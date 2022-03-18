# https://www.acmicpc.net/problem/1541
# 백준 1541 - 잃어버린 괄호

'''
최소값을 만들기 위해 '-'가 시작되고
다시 '-'가 나올 떄 까지의 수들을 모두 더해준다
'''

import sys
input = sys.stdin.readline

n = input().split('-')  # '-'를 제외하고 스플릿

sum = 0

for i in n[0].split('+'):   # 0번째 인덱스의 모든 수들을 더해줌
    sum += int(i)

for i in n[1:]: # 0번째 이후 모든 수들을 돌면서
    for j in i.split('+'):  # 그 수들을 '+'를 제외하고 스플릿(각각의 수들로 쪼개짐)
        sum -= int(j)   # 각각의 수들로 쪼개진 수들을 전부 '-' 해주고 sum에 더함

print(sum)