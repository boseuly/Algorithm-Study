class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 시간복잡도 : O(log(N))
    def insert(self, value):
        # 1. 원소를 맨 끝에 추가한다.
        self.items.append(value)
        cur_index = len(self.items) - 1

        # 2. 부모와 비교해서 자기가 높으면 바꾼다.
        while cur_index != 1:
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index] 
                cur_index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
# 1. 맨 뒤에다가 원소를 넣는다.
# 2. 부모와 비교해서 자기가 높으면 바꾼다.
# 3. 2의 과정을 부모가 더 크거나 루트 노드에 달했을 때까지 반복한다.
max_heap.insert(3)
#   3      Level 0
# [None, 3]
max_heap.insert(4)
# 1. 맨 뒤에 넣어준다.
#   3       Level 0
#  4        Level 1

# 2. 부모와 비교했을 때 4 > 3(부모) 이므로 둘을 바꿔준다.
# [None, 4,3]

max_heap.insert(2)
#       4       Level 0
#     3   2     Level 1
# [None, 4,3,2]

max_heap.insert(9)
# 1. 맨 뒤에 넣어준다.
#       4       Level 0
#     3   2     Level 1
#   9           Level 2

# 2. 부모와 비교했을 때 9 > 3 (부모) 이므로 둘을 바꿔준다. 
# 3. 2의 과정을 부모가 더 크거나 루트 노드에 달했을 때까지 반복한다.
# [None, 9,4,2,3]
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!

