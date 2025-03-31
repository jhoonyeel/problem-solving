def solution(my_str, n):
    lst = []
    for x in range(0, len(my_str), n):
        lst.append(my_str[x:x + n])
    return lst
    # 반올림 판별. 나머지가 0이 아닐 때, +1 해주기.