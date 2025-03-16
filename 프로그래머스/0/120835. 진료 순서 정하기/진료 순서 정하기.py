def solution(emergency):
    N = len(emergency)
    res = [0] * N
    last_big = 0
    for order in range(N):
        biggest = 0
        for el in emergency:
            if not last_big:
                if biggest < el:
                    biggest = el
            else:
                if biggest < el and el < last_big:
                    biggest = el
        res[emergency.index(biggest)] = order + 1
        last_big = biggest
    return res