# [제공된 함수]
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0]* 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')            # 'a' = 97, 알파벳 'b'= 98 이므로 98- 97 = 1, index 1에는 'b'가 저장된다.
        alphabet_occurrence_array[arr_index] += 1   # count하기 위해서 + 1

    return alphabet_occurrence_array

# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.
# "abadabac" # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

input = "abadabac"
# [강사풀이]
def find_not_repeating_first_character(string):
    # 반복되지 않는 첫번째 알파벳
    # 반복되는지 아닌지를 판단
    # alphabet_occurrence_array
    # string 에서 알파벳의 빈도수를 찾는다.
    occurrence_array = find_alphabet_occurrence_array(string)
    not_repeating_character_array = []
    # occurrence_array에서 1로 표기되어 있는 값들의 알파벳을 가지고 와야 한다.
    # 값이 1인 알파벳들을 찾아서 저장한다.
    # O(26) => 상수만큼의 연산은 무시해도 된다. (occurrence_array는 항상 길이가 26이므로(a~z))
    for index in range(len(occurrence_array)):
        alphabet_occurrence = occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))

    # 어떤 값이 첫 번째 값인지 확인하는 작업
    # 시간복잡도 O(N)
    for char in string:
        if char in not_repeating_character_array:
            return char
    return "_"
result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))

