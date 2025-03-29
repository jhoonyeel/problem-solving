def tuned(current):
    next_lst = []
    for el in current:
        if el >= 50 and el % 2 == 0:
            next_lst.append(el // 2)
        elif el < 50 and el % 2 != 0:
            next_lst.append(2 * el + 1)
    return next_lst

def solution(arr):
    cnt = 0
    lst, next_lst = arr[:], tuned(arr) # 0번 반복
    N = len(arr)
    while lst != next_lst:
        lst, next_lst = next_lst, tuned(next_lst)
        cnt += 1
    return cnt - 1
    # lst == next_lst 는 주소 비교 X. 리스트 요소와 순서 판별.
    # set(lst) != set(next_lst)는 순서 판별 X.