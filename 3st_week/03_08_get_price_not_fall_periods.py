from collections import deque
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 함수를 완성하세요.
#
# prices = [1, 2, 3, 2, 3]
# answer = [4, 3, 1, 1, 0]
prices = [ 1, 2, 3, 2, 3]
#            0
#               1  2  3  4
#               1
#                  2  3  4


# [내풀이]
def get_price_not_fall_periods(prices):
    # 이중 for문 필요
    # count 를 저장하는 변수가 필요함
    answer = [0] * len(prices)

    for i in range(len(prices)):
        print(i)
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer[i] = count

    return answer


# [강사풀이1 - 일반풀이]
def get_price_not_fall_periods1(prices):
    answer = [0] * len(prices)

    for i in range(0, len(prices) - 1, 1):
        price_not_fall_period = 0
        for j in range(i + 1, len(prices), 1):
            if prices[i] <= prices[j]:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        answer[i] = price_not_fall_period
    return answer


# [강사풀이1 - 큐 사용 풀이]
def get_price_not_fall_periods_queue(prices):
    prices_queue = deque(prices) # 이렇게하면 prices 배열을 queue로 변환할 수 있음
    result = []
    while prices_queue: # prices_queue가 비어있지 않다면 반복한다.
        price_not_fall_period = 0
        current_price = prices_queue.popleft()
        for next_price in prices_queue:
            if current_price <= next_price:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        result.append(price_not_fall_period) # stack에 값을 넣어준다.

    return result



# print(get_price_not_fall_periods1(prices))
#
# print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods1(prices))
# print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods1([3, 9, 9, 3, 5, 7, 2]))
# print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods1([1, 5, 3, 6, 7, 6, 5]))

print(get_price_not_fall_periods_queue(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_queue(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_queue([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_queue([1, 5, 3, 6, 7, 6, 5]))

# 복습
# stack은 처음으로 들어간 데이터가 마지막으로 나온다. => FILO 방식
# stack에 포함된 함수로는 push, pop, peek, is_empty

# queue는 처음 들어간 데이터가 첫번째로 나온다. => FIFO 방식
# queue에 포함된 함수는 enqueue, dequeue, peek, is_empty

