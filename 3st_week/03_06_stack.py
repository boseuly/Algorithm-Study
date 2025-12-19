# 스택 공부
# Linked List 와 같이 스택을 공부해보자
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List는 화물칸(노드) 들을 하나하나 이어지도록 만든 개념이 링크드 리스트였음

# Stack의 개념
# 1. 한 곳에서만 자료를 넣고 뺄 수 있다.
# 2. LIFO -> Last in first out -> 가장 마지막에 넣은 게 가장 빨리 나온다.
# 3. 함수는 push, pop, peek가 있음
# [4] -> [3] 3이 마지막으로 들어 왔으니, 가장 먼저 빠져나간다.




class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)      # [3] 이라는 노드를 만듦.
        new_head.next = self.head   # [3] -> [4]
        self.head = new_head        # [3] 이라는 노드를 head로 만들어줌

    # pop기능구현
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        delete_head = self.head
        self.head = self.head.next  # head의 값을 다음 값으로 만들기만 하면 됨
        return delete_head          # 삭제된 값을 전달해야 됨

    # peek기능구현
    def peek(self):
        if self.is_empty():
            print("stack is empty")
        return self.head.data

    # head값이 비어 있는지 안 비어 있는지 여부를 전달하는 함수
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
stack.push(5)
print(stack.peek())
stack.pop()
print(stack.peek())

stack.pop()
stack.pop()
stack.pop()

# 실제로 구현해봤지만, 실제 코드에서는 파이썬의 list를 이용해서 스택을 사용한다.
# stack = []        # 빈 스택 초기화
# stack.append(4)   # 스택 push(4)
# stack.append(3)   # 스택 push(3)
# top = stack.pop() # 스택 pop

