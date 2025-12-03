# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# # 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]
input = 20

# [내 풀이]
def find_prime_list_under_number(number):
    # for문을 2~number까지 돌린다.
    # 이중 for문 사용
    # 첫번째 for문에는 2~number만큼 돌리고
    # 두번째 for문은 2~num만큼 돌린다. (첫번째 for문의 숫자보다 작은 수만큼!)
    # number를 num으로 나눴을 때 만약 나머지가 0이라면 소수가 아니므로 decimal_yn은 False -> break
    # number를 num으로 나눴을 때 모두 나머지가 0이 아니라면 소수이므로 decimal_yn은 True -> decimal배열에 append

    decimal = []
    if number > 1: # 1보다 크다면
        for num in range(2, number):
            decimal_yn = True
            for under_number in range(2, num):
                if num % under_number == 0:
                    decimal_yn = False   # 만약 나눠진다면 소수가 아니므로 break
                    break

            if decimal_yn:
                decimal.append(num)
    return decimal

result = find_prime_list_under_number(input)
print(result)