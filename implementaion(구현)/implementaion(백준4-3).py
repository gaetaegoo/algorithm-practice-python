# implementaion(구현) 실전 문제
# 왕실의 나이트 - p.115

import sys
input = sys.stdin.readline

input_data = input()
row = int(input_data[1])
'''
ord는 문자를 아스키코드로 바꿔줌
'a'는 아스키코드로 97인데, 들어오는 문자에서 항상
97만큼 빼줘야 컬럼(문자)을 인트(정수)로 표현 가능
'c가' 입력된 예: 'c'(99) - 'a'(97) + 1 = 3 
'''
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 말이 이동할 수 있는 (최대)8가지 범위
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for step in steps:
    # row와 column 인덱스는 바껴도 될 듯?
    new_row = row + step[0]
    new_column = column + step[1]

    if new_row >= 1 and new_row <= 8 and new_column >=1 and new_column <=8:
        result += 1

print(result)
