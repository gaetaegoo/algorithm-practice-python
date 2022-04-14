N = int(input())                    # 토핑 종류 수
A, B = map(int, input().split())    # A: 도우 가격 / B: 토핑 가격
C = int(input())                    # 도우 칼로리
D = []
for i in range(N):                  # 토핑 칼로리
    D.append(int(input()))

D.sort(reverse=True)

result = 0  # 최고의 피자(1 달러 당 최대의 열량)
kcal = 0    # 토핑 칼로리
price = 0   # 토핑 가격

for i in D:     # 토핑들을 돌면서
    kcal += i   # for문이 돌 때 마다 각 토핑들 칼로리 추가
    price += B  # 토핑이 추가될 때 마다 토핑 가격 추가

    cal = (kcal + C) / float(price + A)  # 도우+피자 칼로리 / 도우 + 피자 가격
    if cal < result:    # 현재 계산된 열량이 result(저장된 칼로리)보다 낮다면 종료
        break
    else:               # 그게 아니라면 cal을 result에 저장
        result = cal

print(int(result))
