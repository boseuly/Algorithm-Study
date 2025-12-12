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

    # Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
    # [내풀이]
    def get_kth_node_from_last(self, k):
        # linked_list를 for문을 돌면서 카운트를 하고
        # 그 숫자가 k일 때 return을 한다.
        # [5] -> [6] -> [7] -> [8] -> [9]
        # 5개의 list가 있을 때 3번째라고 하면 3번째 (5-3)+1
        # 9개의 리스트 뒤에서 2번째 -> 앞에서 (9-2)+1 번째임
        # 즉 (n-k)+1번째 값을 리턴하면 됨
        # 1 2 3 4 5 6 7 8 9

        cur_for_total_length = self.head
        total_length = 0

        while cur_for_total_length.data is not None:
            total_length += 1

            if cur_for_total_length.next is None: break
            cur_for_total_length = cur_for_total_length.next

        cur = self.head
        current_index_count = 0  # 현재 몇 번째인지 카운트할 용도
        find_index = (total_length - k) + 1  # 해당 번째에 반환해야 함

        while cur.data is not None:
            current_index_count += 1
            if current_index_count == find_index:  # 만약 count와 k의 값이 같아진다면 반환
                return cur
            cur = cur.next
        return cur


# [강사풀이]
class Node1:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedLis1t:
    def __init__(self, value):
        self.head = Node1(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node1(value)

    # [강사풀이 - 1] 시간복잡도: O(N)
    def get_kth_node_from_last_1(self, k):
        length = 1  # 차이점.. 나는 0부터 잡았음
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1
        end_length = length - k  # 나는 length를 0부터 잡아서 + 1을 해줌
        cur = self.head

        for i in range(end_length):
            cur = cur.next
        return cur

    # [강사풀이 - 2] 시간복잡도: O(N)
    def get_kth_node_from_last_2(self, k):
        # slow와 fast 이용하기
        # 현재지점이 slow에서 k 만큼 떨어진 fast가 마지막 지점까지 도달할 때
        # slow가 바로 뒤에서 k만큼 떨어진 값이 된다.!!
        slow = self.head
        fast = self.head

        for i in range(k): # k만큼 먼저 보낸다.
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow




linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
# print(linked_list)

print(linked_list.get_kth_node_from_last(4).data)  # 7이 나와야 합니다!
