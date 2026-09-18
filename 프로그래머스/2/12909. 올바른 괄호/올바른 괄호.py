## 풀이
# '((((((('상황을 생각함.
# 왼쪽 괄호 개수를 계속 저장하는 구조임.
# 따라서, 왼쪽 괄호 개수를 저장하는 변수를 두고, 오른쪽 괄호를 만나면 하나씩 빼도록 구현함.

def solution(s):
    left = 0
    for el in s:
        if el == '(':
            left += 1
        else:
            left -= 1
            if left < 0:
                return False

    return left == 0