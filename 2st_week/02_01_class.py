
class Person:
    # 생성자 함수를 통해서 객체가 어떤 속성을 가지고 있는지 선언해준다.
    def __init__(self, name_param): # self는 객체 자기 자신을 의미
        self.name = name_param
        print("hihi i am created", self, self.name)

    def talk(self):
        print("안녕하세요 저는 ", self.name, "입니다.")


person_1 = Person("유재석") # 객체마다 주소가 서로 다름
print(person_1.name)
person_1.talk()

person_2 = Person("박명수")
print(person_2.name)
person_2.talk()