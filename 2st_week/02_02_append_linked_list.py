class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(5)
# print(node.data, node.next)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # LinkedList의 가장 끝에 있는 노드에 새로운 노드를 연결해줘
    # 현재 상태
    # [5] -> [3] -> [7] -> [6] -> [8] -> None

    # 요청 반영된 상태
    # [5] -> [3] -> [7] -> [6] -> [8] -> [9](new)

    # Node의 next를 쭉 살펴보면 맨 마지막 노드의 next 값으 None이 나온다.
    # 그럼 해당 노드의 next에 [9] 노드를 추가해주면 됨

    # next 노드 추가해주는 로직
    def append(self, value):
        cur = self.head
        while cur.next is not None: # cur.next가 None이 아닌 경우까지만
            cur = cur.next

        cur.next = Node(value)

    # linked_list에서 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력해주는 함수
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data) # 현재 데이터를 출력해주고
            cur = cur.next  # next데이터를 다시 cur에 넣어준다.

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()
# [5] -> [12] -> [8]


