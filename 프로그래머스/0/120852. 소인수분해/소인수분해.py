def solution(n):
    res = []
    for x in range(2, n + 1):
        isSoinsu = True
        for y in res:
                if x % y == 0:
                    isSoinsu = False
                    break
        if n % x == 0 and isSoinsu:
            res.append(x)
    return res