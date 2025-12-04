# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.
# "abadabac" # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

input = "abadabac"
# [내풀이]
def find_not_repeating_first_character(string):
    # 이중 for문을 돌려서 문자열 하나하나 반복되는 문자가 있는지 확인한다.
    # 만약 반복되는 것이 하나라도 있다면 for문을 break해서
    # 첫번째 for문에서 해당 값을 저장해준다.
    for element in string:
        single_occurrence_string = ""
        repeating_count = 0 # 2번 이상 발생되면 반복되는 문자임

        for comparison_string in string:
            if comparison_string == element:    # 값이 서로 같다면
                repeating_count += 1            # 카운트 저장
                if repeating_count > 1:
                    break                       # 두번 이상이면 for문 멈춰준다.

        if repeating_count <= 1: # 만약 repeating_count가 1개 이상이면
            return element      # 해당 문자값을 single_occurrence_string에 저장해준다.

    return "_"
result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
