# queue는 먼저 들어간 값이 먼저 나온다.
# FIFO (first in first out)
# 순서대로 처리되어야 할 때 사용된다.

# enqueue(data): 맨 뒤에 데이터 추가
# dequeue(): 맨 앞의 데이터 뽑기
# peek(): 맨 앞의 데이터 보기
# isEmpty(): 큐가 비었는지 안 비었는지 여부 반환

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 맨 뒤에 값이 추가된다.
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    # 맨 앞에 있는 값을 빼는 함수
    def dequeue(self):
        # 어떻게 하면 될까요?
        # head 값에 next값을 넣어준다.
        if self.is_empty():
            return print("Queue is empty")

        delete_head = self.head
        self.head = self.head.next

        return delete_head

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            print("Queue is empty")
            return
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
# print(queue.peek())
queue.enqueue(4)
queue.enqueue(5)
# print(queue.peek())
queue.enqueue(6)
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())