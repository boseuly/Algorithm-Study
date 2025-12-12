# 재귀함수와 팩토리얼
# 3! = 3*2*1
# factorial(n) = n * factorial(n-1)
# factorial(n-1) = (n-1) * factorial(n-2)
# factorial(n-2) = (n-2) * factorial(n-3)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))

