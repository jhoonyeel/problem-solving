def tuned(current):
    next_lst = []
    for el in current:
        if el >= 50 and el % 2 == 0:
            next_lst.append(el / 2)
        elif el < 50 and el % 2 != 0:
            next_lst.append(2 * el + 1)
    return next_lst

def solution(arr):
    cnt = 0
    lst, next_lst = arr[:], tuned(arr) # 0번 반복
    N = len(arr)
    while set(lst) != set(next_lst):
        lst, next_lst = next_lst, tuned(next_lst)
        cnt += 1
    return cnt - 1