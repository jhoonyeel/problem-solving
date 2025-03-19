def solution(array):
    res = 0
    for x in array:
        res += str(x).count('7')
    return res