def solution(n):
    res = []
    for x in range(2, n + 1):
        flag = True
        for y in res:
                if x % y == 0:
                    flag = False
                    break
        if n % x == 0 and flag:
            res.append(x)
    return res