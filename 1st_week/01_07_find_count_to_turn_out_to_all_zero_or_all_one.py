# for ~ else 문 : for문을 도는 모든 값이 특정 값인지 확인할 때 주로 사용한다.
# for x in [1,2,3,4]:
#     print(x)
#     if x == 4:
#         break
# else:
#     print("완료되었습니다.")

# Q.
# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
# 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
# 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
#
# 예를 들어 S=0001100 일 때,
#
# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
#
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.

# 문자열을 모두 1로 변경한다.
# 주어진 문자열을 for문을 통해 둘러보면서 만약 0이라면 1로 변경하여 다시 저장해줘야 한다.
input = "011110"

# [내풀이]
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    all_turn_string = ""
    for char in string:
        if char == '0':
            all_turn_string += '1'
        else:
            all_turn_string += char
    return all_turn_string

# result = find_count_to_turn_out_to_all_zero_or_all_one(input)
# print(result)

# [강사풀이]
# 0에서 1을 마주쳤을 때 뒤집는다 -> 전체를 0으로 만들기 위한 작업
# 1에서 0을 마주쳤을 때 뒤집는다 -> 전체를 1으로 만들기 위한 작업

def find_count_to_turn_out_to_all_zero_or_all_one_2(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == "1":
        count_to_all_zero += 1
    elif string[0] == "0":
        count_to_all_one += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == "1":
                count_to_all_zero += 1
            if string[i + 1] == "0":
                count_to_all_one += 1
    return min(count_to_all_one, count_to_all_zero)

result = find_count_to_turn_out_to_all_zero_or_all_one_2(input)
print(result)
