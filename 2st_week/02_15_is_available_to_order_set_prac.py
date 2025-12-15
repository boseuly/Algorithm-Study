# !!! 헷갈리는 문제 다시 풀어보기 !!!
# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오. (hint !! 정렬 sort() 사용)


shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)  # O(N)
    for order in orders:    # O(M)
        if order not in menus_set:  # O(1) -> menus_set에 order가 존재하는지 확인하는 로직
            return False
    return True

# 이진탐색 - 문자열에서 해당 문자가 있는지 찾아주는 함수
def is_existing_target_number_binary(target, array):
    start_index = 0
    end_index = len(array) - 1
    pointer_index = (start_index + end_index) // 2

    while start_index <= end_index:
        # array[pointer_index] == target 일 경우
        # return true
        if array[pointer_index] == target:
            return True
        elif array[pointer_index] < target:
            # array[pointer_index] < target 일 경우
            # start_index = pointer_index + 1
            start_index = pointer_index + 1
        else:
            # array[pointer_index] > target 일 경우
            # end_index = pointer_index - 1
            end_index = pointer_index - 1
        pointer_index = (start_index + end_index) // 2

    return False


def is_available_to_order1(menus, orders):
    # menus를 sort한 다음에
    # 이진탐색을 사용한다.
    menus.sort()
    for order in orders:
        if not is_existing_target_number_binary(order, menus):
            return False
    return True


result = is_available_to_order1(shop_menus, shop_orders)
print(result)