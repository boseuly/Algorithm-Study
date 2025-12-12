# Q. 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다.
# 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.
# // 를 사용하면 소수점을 버린 몫을 반환할 수 있음

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = 0
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else: # array[current_guess] > target
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)