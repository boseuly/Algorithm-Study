# 회문검사
# palindrome 은 회문을 의미합니다!
# is_palindrome("토마토")   # True
# is_palindrome("tomato") # False
# is_palindrome("abcba")  # True

input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n-1-i]:
            return False
    return True


print(is_palindrome(input))