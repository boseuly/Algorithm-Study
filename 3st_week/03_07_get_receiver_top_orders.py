
top_heights = [6, 9, 5, 7, 4]


# 송수신하는 탑을 반환해야 한다.
# 일반 풀이 (stack 사용 x)
def get_receiver_top_orders(heights):
    # heights.reverse()   # 끝부터 살펴봐야하기 때문에
    # 1 2 3 4
    # --------
    # 4 3 2 1
    # 3 2 1
    # 2 1
    # O(N^2)

    answer = [0] * len(heights)
    for i in range(len(heights) - 1, 0 , -1): # len(heights) -1 ~ 1, -1씩 감소
        print('i : ',i)
        for j in range(i - 1, -1, -1):  # i-1 ~ 0, -1씩 감소
            if heights[i] <= heights[j]:
                answer[i] = j + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

# print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
# print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
# print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))