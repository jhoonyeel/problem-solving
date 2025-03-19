def solution(s):
    lst = [x for x in s if s.count(x) == 1]
    return ''.join(sorted(lst))