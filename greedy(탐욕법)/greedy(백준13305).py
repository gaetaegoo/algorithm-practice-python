import sys
input = sys.stdin.readline

n = int(input())                    # 도시의 개수
k = list(map(int, input().split())) # 도시간 거리
l = list(map(int, input().split())) # 도시별 기름 가격

sum_cost = 0       # 총 드는 최소 비용
min_cost = l[0]    # 가장 싼 도시의 기름 가격

for i in range(n-1):        # 마지막 도시(=도착지)의 기름 가격은 필요 없으므로 n-1
    if min_cost > l[i]:     # 만약 지금 도시의 기름 가격 보다, 새로운 도시의 기름 가격이 싸다면
        min_cost = l[i]     # 그 가격을 최소 가격에 대입하고
    sum_cost += (min_cost * k[i])    # 기름값 * 도로 길이를 곱한 값을 최종 대입

print(sum_cost)