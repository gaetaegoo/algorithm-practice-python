# 5-3 재귀 함수 예제
# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()
#
# recursive_function()


# # 5-4 재귀 함수 종료 예제
# def recursive_function(i):
#     # 10번째 출력했을 때 종료되도록 조건 명시
#     if i == 10:
#         return
#     print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
#     recursive_function(i + 1)
#     print(i, '번째 재귀 함수를 종료합니다.')
#
# recursive_function(1)

# 5-5 2가지 방식으로 구현한 팩토리얼(n!) 예제
def factorial_iterative(n): # 반복문으로 구현한 n!
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n): # 재귀적으로 구현한 n!
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
