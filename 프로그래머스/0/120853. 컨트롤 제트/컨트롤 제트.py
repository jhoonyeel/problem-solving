def solution(s):
    lst = s.split()
    total = 0
    for i, v in enumerate(lst):
        if v == 'Z':
            total -= int(lst[i - 1])
        else:
            total += int(v)
    return total