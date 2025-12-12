# 재귀함수를 통해서 회문검사를 할 수 있음

input = '소주만병만주소'
def is_palindrome(string):
    if string[0] != string[-1]: # 맨 앞 글자와 맨 뒷 글자가 서로 다르면 False
        return False
    if len(string) == 1: # 글자가 한 글자라면 무조건 회문에 해당함
        return True

    # string이 '소주민병만주소' 라면
    # '주만병만주'를 다시 전달해주고
    # '만병만'을 다시 전달해주고
    # '병'을 전달해주면 결국 회문검사에서 True가 반환된다.
    return is_palindrome(string[1:-1])

print(is_palindrome(input))
