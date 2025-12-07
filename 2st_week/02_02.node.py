# Node클래스 만들기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 3을 가진 Node를 만들려면 아래와 같이 작성해주면 된다.
node = Node(3) # 현재는 next가 없이 하나의 노드만 있음

# node 만들어보기
first_node = Node(5)
second_node = Node(12)
first_node.next = second_node # [5]의 next를 [12]로 지정한다. [5] -> [12]
# [5] -> [12] -> [7] -> [6]
third_node = Node(7)
second_node.next = third_node

fourth_node = Node(6)
third_node.next = fourth_node

# 이런식으로 계속 노드를 연결해주는 작업을 하면 너무 번거로움
# LinkedList라는 클래스를 만들어서 자동으로 노드가 연결되도록 해준다.

# 1) LinkdList는 self.head에 시작하는 노드를 저장한다.
# 2) 다음 노드를 보기 위해서는 각 노드의 next를 조회해서 찾아가야 한다.




