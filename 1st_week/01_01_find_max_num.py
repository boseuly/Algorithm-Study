# 숫자를 하나씩 비교해가면서 가장 큰 값을 찾는다.
# 어떻게 비교해야할까
# 변수에 array의 첫번째 값을 저장한 다음에
# for문을 돌리면서 현재값보다 큰 값이 있는지 확인
# 만약 현재값보다 크다면 해당 값을 저장
# [내 풀이]
def find_max_num(arr):
    result = arr[0]
    # 이 부분 직접 채워보기
    for i in range(len(arr)):
        if result < arr[i]:
            result = arr[i]
    return result
print("정답 = 84 / 현재 풀이 값 = ", find_max_num([12,3,4,5,7,84,4,7,9,4,2]))
print("정답 = 12 / 현재 풀이 값 = ", find_max_num([12,3,4,5,5,6,7,8,3,2,10]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6,7,8,9,3,1888]))


# [강의 풀이]
def find_max_num2(array):
    for number in array:
        is_max_num = True
        for compare_number in array:
            if number < compare_number:
                is_max_num = False
            if is_max_num:
                return number

# [강의풀이2]
def find_max_num3(array):
    max_number = array[0]
    for number in array:
        if number > max_number:
            max_number = number
    return max_number

