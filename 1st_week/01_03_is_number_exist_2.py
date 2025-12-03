# Q. 다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False 를 반환하시오.
# [강사풀이]
def is_number_exist(number, array):
    for element in array:       # array의 길이만큼 아래 연산이 실행
        if element == number:   # 비교 연산 1번 실행
            return True         # 시간복잡도는 N만큼 걸린다.
    return False

result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))  # 운이 좋은 경우 !! 시간복잡도가 1밖에 안 걸린다. -> 최선의 경우에는 1만큼의 연산만 필요하다.
# 3은 array의 첫 번째 인덱스에 있기 때문에 for문을 다 돌지 않아도 된다.
print("정답 = True 현재 풀이 값 =", result(4, [3,5,6,1,2,4]))  # 운이 좋지 않은 경우 !! 시간복잡도가 N만큼 걸린다. -> 최선의 경우에는 N만큼의 연산이 필요하다.
# 파라미터로 어떤 값을 갖느냐에 따라서 for문을 다 돌아야 한다.
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))


# 빅오 -> 최악의 경우
# 빅오메가 -> 최선의 경우
