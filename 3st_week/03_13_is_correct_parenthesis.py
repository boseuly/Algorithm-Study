#Q. 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어
# ()() 또는 (())() 는 올바르다.
# )()( 또는 (()( 는 올바르지 않다.
#
# 이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.
# [내 풀이]
def is_correct_parenthesis(string):
    # string 을 한 글자씩 가지고 온다.
    # dict= {"(" : 1, ")" : 1} 이런 형식으로 여는 괄호와 닫는 괄호의 노출 수를 저장한다.
    # "("와 ")"가 등장할 때마다 수를 늘려준다
    # <조건>
    # 첫 글자는 무조건 "("로 시작해야 한다.
    # 마지막 글자는 무조건 ")" 로 끝나야 한다.
    # ")" 와 "("의 수는 같아야 한다.

    dict = { "(" : 0, ")": 0}
    open_str = "("
    close_str = ")"
    index = 0
    for str in string:
        if index == 0 and str != open_str: # 첫 글자는 무조건 "(" 로 시작되어야 한다.
            return False

        if index == len(string) - 1 and str != close_str: # 마지막 글자는 무조건 ")"로 끝나야 한다.
            return False
        dict[str] += 1
        index += 1

    if dict[open_str] == dict[close_str]:
        return True

    return False

# [강사풀이]
def is_correct_parenthesis_1(string):
    # Stack 을 사용한다.
    stack = []
    for i in range(len(string)):
        if string[i] =="(":
            stack.append("(")
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    # stack이 비어있지 않다면 False
    if len(stack) != 0:
        return False
    else:
        return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
