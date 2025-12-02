# Q.다음과 같은 문자열을 입력 받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환
# [강의풀이1]
# 1. a~z까지 배열에 저장
# 2. for문으로 돌면서 해당 문자열의 발생 건수를 occurrence에 저장
# 3. 저장된 occurrence와 max_occurrence를 비교해서 더 큰 것을 max_occurrence에 저장
def find_max_occurred_alphabet_answer(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                      "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    max_occurred = 0
    max_alphabet = alphabet_array[0] #a

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurred:
            max_occurred = occurrence
            max_alphabet = alphabet

    return max_alphabet

# [강의풀이2]
# 1. 각 알파벳이 몇 번 출현했는지 하나의 배열에 저장
# 2. 알파벳 출현 횟수를 for문을 통해서 비교
# 3. 출현 횟수가 가장 많은 인덱스를 찾고 아스키코드를 통해서 해당 인덱스에 맞는 알파벳을 return

def find_max_occurred_alphabet_answer_2(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')    # 해당 문자를 인덱스로 치환 ex) 'a' -> 0, 'b' -> 1
        alphabet_occurrence_array[arr_index] += 1 # 해당 인덱스에 +1해준다.

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)): # 0, 1, ..., 25
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
    return chr(max_alphabet_index + ord('a'))


result1 = find_max_occurred_alphabet_answer
print("정답 = i 현재 풀이 값 = ", result1("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 = ", result1("we love algorithm"))
print("정답 = b 현재 풀이 값 = ", result1("best of best youtube"))

