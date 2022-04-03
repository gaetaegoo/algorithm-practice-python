# https://codeup.kr/problem.php?id=6068
# 6068 : 점수 입력받아 평가 출력하기

'''
점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

평가 기준
점수 범위 : 평가
 90 ~ 100 : A
 70 ~   89 : B
 40 ~   69 : C
   0 ~   39 : D
로 평가되어야 한다.
'''

# 'elif'로 축약시키지 않은 코드
# 코드가 길고 가독성이 떨어짐
n = int(input())

if n >= 90:
    print('A')
else:
    if n >= 70:
        print('B')
    else:
        if n > 40:
            print('C')
        else:
            print('D')

# 위 코드와 같으면서 'elif'로 축약시킨 코드
# 코드가 짧고 가독성이 좋아짐
n = int(input())

if n >= 90:
    print('A')
elif n >= 70:
    print('B')
elif n >= 40:
    print('C')
else:
    print('D')