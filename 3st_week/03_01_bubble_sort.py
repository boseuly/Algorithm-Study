# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 버블 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1]

#  n
# 3,1,2 -> 1,3,2 -> 1,2,3
#  n -1
# 1,2,3
# 2,5,7,6,8,3,4,1



def bubble_sort(array):
    n = len(array)

    # 시간복잡도 O(N^2)
    for i in range(n - 1):
        for j in range(n - i - 1): # i를 빼는 이유는 i만큼은 이미 정렬이 된 상태이기 때문에
            if array[j] > array[j + 1]: # 만약 array[j]보다 array[j+1]이 더크면 값을 서로 바꿔줘야 한다.
                array[j], array[j+1] = array[j+1], array[j]

    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))