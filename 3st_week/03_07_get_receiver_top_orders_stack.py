
top_heights = [6, 9, 5, 7, 4]


# 송수신하는 탑을 반환해야 한다.
# stack 사용 풀이
def get_receiver_top_orders(heights):
    # heights.reverse()   # 끝부터 살펴봐야하기 때문에
    # 1 2 3 4
    # --------
    # 4 3 2 1
    # 3 2 1
    # 2 1
    # O(N^2)
    answer = [0] * len(heights)
    while heights:                                  # O(N)
        height = heights.pop()
        for i in range(len(heights) - 1, -1, -1):   # O(N)
            if height <= heights[i]:
                answer[len(heights)] = i + 1
                break

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

# print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
# print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
# print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))