def solution(emergency):
    N = len(emergency)
    res = [0] * N
    last_big = 10 ** 9
    for order in range(1, N + 1):
        biggest = 0
        for el in emergency:
            if biggest < el < last_big:
                biggest = el
        res[emergency.index(biggest)] = order
        last_big = biggest
    return res