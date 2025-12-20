# dict = {"fast": "빠른"}
# dictionary의 인덱스(키) 충돌을 방지하기 위해서
# Chaining 방식을 사용한다.
# 이외에도 개방주소법 이라는 방법이 있음
# 찾은 인덱스에 이미 값이 차 있다면 그 다음 값에 데이터를 저장하는 것임
class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

linked_tuple = LinkedTuple()
linked_tuple.add("123", "linked")
linked_tuple.add("456", "tuple")
print(linked_tuple.items)
print(linked_tuple.get("123"))


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key) # LinkedTuple [(key, value),(key, value)] 여기서 key 값에 해당하는 value를 반환해야 됨


my_dict = LinkedDict()
my_dict.put("test", 3)
print(my_dict.get("test"))
