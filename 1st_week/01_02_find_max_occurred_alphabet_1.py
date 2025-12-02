# Q.다음과 같은 문자열을 입력 받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환

# 문자열 공백을 제거한 다음에 해당 문자열을 리스트로 만든다.
# 그리고 해당 문자열들을 count()를 통해서 센다.
# cnt변수, result 변수 필요
# cnt변수에 저장된 값을 기준으로 비교를 진행
# [내 풀이1]
def find_max_occurred_alphabet(string):
    str_list = list(string.replace(" ", ""))
    res = str_list[0]   # 반환할 문자
    count = 0           # 비교할 숫자
    for a in str_list:
        if not a.isalpha():
            continue
        if count < str_list.count(a):
            count = str_list.count(a)
            res = a

    return res

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 = ", result("hello my name is dingcodingco")) # o, i 모두 3번 출력되는 상황이라서 o도 정답 인정?
print("정답 = e 현재 풀이 값 = ", result("we love algorithm"))
print("정답 = b 현재 풀이 값 = ", result("best of best youtube"))

# [내 풀이1]
def find_max_occurred_alphabet2(string):
    count_array = find_alphabet_occurrence_array(string)    # 각 알파벳별 카운트 결과
    max_counting_number = 0
    max_alphabet = ""
    index = 0
    for num in count_array:
        if num > max_counting_number:
            max_counting_number = num
            max_alphabet = chr(index + ord('a')) # 결과값을 저장
        index += 1
    return max_alphabet

# [제공된 함수]
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0]* 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')            # 'a' = 97, 알파벳 'b'= 98 이므로 98- 97 = 1, index 1에는 'b'가 저장된다.
        alphabet_occurrence_array[arr_index] += 1   # count하기 위해서 + 1

    return alphabet_occurrence_array

result1 = find_max_occurred_alphabet2
print("정답 = i 현재 풀이 값 = ", result1("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 = ", result1("we love algorithm"))
print("정답 = b 현재 풀이 값 = ", result1("best of best youtube"))