# Q.  다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.
#
# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.
#
# 단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.

# [6] -> [7] -> [8]
# [3] -> [5] -> [4]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


# [내풀이]
def get_linked_list_sum(linked_list_1, linked_list_2):
    linked_value_join_1 = ''
    linked_value_join_2 = ''
    cur_1 = linked_list_1.head
    cur_2 = linked_list_2.head

    # linked_list 안에 값을 for문을 통해서 저장한다.
    while cur_1 is not None: # 값이 없을 때까지
        linked_value_join_1 += str(cur_1.data)
        cur_1 = cur_1.next

    while cur_2 is not None:  # 값이 없을 때까지
        linked_value_join_2 += str(cur_2.data)
        cur_2 = cur_2.next

    return int(linked_value_join_1) + int(linked_value_join_2)



# [강사풀이1] - 반복되는 코드를 함수로 뺄 수 있는 상황
def get_linked_list_sum1(linked_list_1, linked_list_2):
    sum_1 = 0
    cur_1 = linked_list_1.head
    while cur_1 is not None:
        sum_1 = sum_1 * 10 + cur_1.data
        cur_1 = cur_1.next

    sum_2 = 0
    cur_2 = linked_list_2.head
    while cur_2 is not None:
        sum_2 = sum_2 * 10 + cur_2.data
        cur_2 = cur_2.next

    return sum_1 + sum_2


# [강사풀이2] - 반복되는 코드를 함수로 뺀 풀이
def get_single_linked_list_sum(linked_list):
    sum = 0
    cur = linked_list.head

    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next

    return sum

def get_linked_list_sum1(linked_list_1, linked_list_2):
    sum_1 = get_single_linked_list_sum(linked_list_1)
    sum_2 = get_single_linked_list_sum(linked_list_2)
    return sum_1 + sum_2






linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))