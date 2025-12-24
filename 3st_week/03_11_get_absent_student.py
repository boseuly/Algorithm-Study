#Q. 오늘 수업에 많은 학생들이 참여했습니다. 단 한 명의 학생을 제외하고는 모든 학생이 출석했습니다.

# 모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때, 출석하지 않은 학생의 이름을 반환하시오.
all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# 1. 2중 반복문 사용 O(N^2)



# 2. 정렬 방법 사용 O(NlogN)

# Dictionary, Hash Table 사용하는 방법 O(N + N) => O(N)
def get_absent_student(all_array, present_array):
    # 구현해보세요!
    dict = {}
    for key in all_array:
        dict[key] = True

    # 참여한 사람들은 제외시킨다.
    for key2 in present_array:
        dict.pop(key2)

    for k in dict.keys():
        return k
    return None

# Dictionary, Hash Table 사용하는 방법 O(N + N) => O(N)
def get_absent_student1(all_array, present_array):
    # 구현해보세요!
    dict = {}
    for student in all_array:
        dict[student] = True

    # 참여한 사람들은 제외시킨다.
    for present_student in present_array:
        del dict[present_student]

    for key in dict.keys():
        return key
    return None


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))