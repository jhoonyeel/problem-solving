def solution(array, n):
    N = len(array)
    minus_lst = []
    for x in sorted(array):
        minus_lst.append(abs(n - x))
    return sorted(array)[minus_lst.index(min(minus_lst))]
