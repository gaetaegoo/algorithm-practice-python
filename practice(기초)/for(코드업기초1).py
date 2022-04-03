# https://codeup.kr/problem.php?id=6080
# 6080 : 주사위 2개 던지기

'''
1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력해보자.
'''

n, m = map(int, input().split())

# 아주 기초적인 2중 for문
for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)
