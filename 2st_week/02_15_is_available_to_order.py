# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오. (hint !! 정렬 sort() 사용)

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 정렬을 한 다음에 shop_orders만큼 for문을 돌리고
    # 하나씩 값을 찾는다.
    #
    menus.sort()  # ['떡볶이', '만두', '사이다', '오뎅', '콜라']
    orders.sort()  # ['만두', '오뎅', '콜라']

    print(menus, orders)


    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)