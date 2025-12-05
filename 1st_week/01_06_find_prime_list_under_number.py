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
    # number를 num으로 나눴을 때 만약 나머지가 0이라면 소수가 아니므로 prime_yn은 False -> break
    # number를 num으로 나눴을 때 모두 나머지가 0이 아니라면 소수이므로 prime_yn은 True -> decimal배열에 append

    prime_list = []
    if number > 1: # 1보다 크다면
        for num in range(2, number + 1):
            prime_yn = True
            for under_number in range(2, num):
                if num % under_number == 0:
                    prime_yn = False   # 만약 나눠진다면 소수가 아니므로 break
                    break

            if prime_yn:
                prime_list.append(num)
    return prime_list

# 오답:  for num in range(2, number)에서 number+1을 해줘야 하는데 안 해줘서 자기자신에 대한 소수 검증을 하지 않는 상태

result = find_prime_list_under_number(input)
print(result)

# [강사풀이1]
def find_prime_list_under_number_2(number):
    prime_list = []
    # 2~20까지 찾아서
    for n in range(2, number + 1): # 2~n까지의 숫자들이 n에 들어가는 것을 반복한다.
        # 이것들이 소수인가? 소수라면 prime_list에 넣어라!
        for i in range(2, n): # 2부터 n-1까지를 i에 들어가는 것을 반복한다.
            if n % i == 0:  # n % i가 나누어떨어진다면 소수가 아니라는 뜻 그러므로 break를 해서 for문을 멈춘다.
                break       # break를 실행하면 for문의 else문이 작동하지 않음
        else:               # -> 소수일 경우에만 prime_list.append(n) 실행
            prime_list.append(n)
    return prime_list

result = find_prime_list_under_number_2(input)
print(result)

# [강사풀이2 - 더 효율적]
def find_prime_list_under_number_3(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:    # 지금까지 구해놓은 소수로 나눴을 때 나누어 떨어지지 않는다면
            if n % i == 0:      # 소수에 해당함
                break           # 예를 들어, 7을 보면 2,3으로 나누어 떨어지지 않으니 소수에 해당
        else:
            prime_list.append(n)
    return prime_list
result = find_prime_list_under_number_3(input)
print(result)

# [강사풀이3 - 더더 효율적]
# N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다는 수학적 정의를 사용
def find_prime_list_under_number_4(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:    # 지금까지 구해놓은 소수로 나눴을 때 나누어 떨어지지 않는다면
            if i * i <= n and  n % i == 0:      # 소수에 해당함
                break           # 예를 들어, 7을 보면 2,3으로 나누어 떨어지지 않으니 소수에 해당
        else:
            prime_list.append(n)
    return prime_list
result = find_prime_list_under_number_3(input)
print(result)
