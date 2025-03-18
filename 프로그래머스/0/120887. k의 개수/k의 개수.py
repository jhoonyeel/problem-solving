def solution(i, j, k):
    total = 0
    for x in range(i, j + 1):
        total += str(x).count(str(k))
    return total