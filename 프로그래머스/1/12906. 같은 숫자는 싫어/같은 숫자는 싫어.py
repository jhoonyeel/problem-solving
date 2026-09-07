## 오답
# 1. arr를 스택으로 생각함. 들어오는 요소 저장 후 존재하면 넘어가도록 구현함.
# 2. But, "연속된 수"만 제거하는 것이기에 틀림. 따라서, prev 값을 관리함.
# 3. prev 값을 매 순회마다 갱신하고, prev와 현재 요소를 비교하여 저장 여부 관리하도록 풀이.

def solution(arr):
    stk = []
    prev = ''
    for el in arr:
        if el == prev:
            continue
        else:
            stk.append(el)
        prev = el
    
    return stk