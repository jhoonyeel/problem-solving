def solution(array, n):
    return min([(abs(x - n), x) for x in array])[1]
