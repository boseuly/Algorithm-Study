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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    # 특정 인덱스에 노드를 추가해라
    # ["자갈"] -> ["밀가루"] -> ["우편"]
    # ["자갈"] -> ["흑연"]      ["밀가루"] -> ["우편"]
    # ["자갈"] -> ["흑연"] -> ["밀가루"] -> ["우편"]
    # 해당 인덱스의 node를 찾은 다음에 새로운 노드를 중간에 넣어줘라
    def add_node(self, index, value):
        new_node = Node(value)

        # index가 0일 경우 예외처리
        if index == 0:
            new_node.next = self.head   # 현재 head의 값을 new_node의 next에 넣어주고
            self.head = new_node        # head에 new_node를 넣어준다.
            return

        prev_node = self.get_node(index - 1)

        next_node = prev_node.next    # 기존에 연결되어 있던 노드를 저장한다.
        prev_node.next = new_node     # 전 노드와 연결을 해준다.
        new_node.next = next_node       # 기존에 연결되어 있던 노드와 새로운 노드를 연결해준다.

    # 특정 노드 제거
    def delete_node(self, index):
        # index가 0일 경우 예외처리
        if index == 0:
            self.head = self.head.next
            return

        # 해당 인덱스의 전 노드의 next를 변경해준다.
        prev_node = self.get_node(index - 1)  # 이전 노드
        index_node = self.get_node(index)
        prev_node.next = index_node.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(2,17)
linked_list.print_all()
print("------------------")
linked_list.delete_node(1)
linked_list.print_all()

# Linked List는 결국 current 노드임 !!
