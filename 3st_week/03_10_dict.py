# dict = {"fast": "빠른"}

class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        # hash(key) % len(self.items) 값이 동일한 값이 나오면 나중에 저장된 값으로 기존 값을
        # 덮어씌우는데, 이를 충돌이라고 한다.
        # 이러한 충돌을 방지하기 위해 LinkedList의 chaining 을 사용한다.
        # 아래와 같은 방식은 충돌이 발생할 수 있는 로직이다.
        # 03_10_dict_chaining 파일 참고
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
