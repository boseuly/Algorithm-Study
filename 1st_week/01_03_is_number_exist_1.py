# Q. 다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False 를 반환하시오.
# [3, 5, 6, 1, 2, 4]
# [내풀이]
def is_number_exist(number, array):
    # array를 기준으로 for문을 돌린다.
    # array 각 요소(element)를 number와 비교한다.
    # 같다면 exist_yn = true로 변경한다.
    exist_yn = False
    for element in array:
        if element == number:
            exist_yn = True
            break
    return exist_yn

result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))