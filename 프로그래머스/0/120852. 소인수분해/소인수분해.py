def solution(n):
    res = []
    div = 2
    while div <= n:
        if n % div == 0:
            n //= div
            if div not in res:
                res.append(div)
        else:
            div += 1
    return res