def solution(ineq, eq, n, m):
    op = ineq + eq
    d = {
        '>=': lambda a, b: a >= b,
        '<=': lambda a, b: a <= b,
        '>!': lambda a, b: a > b,
        '<!': lambda a, b: a < b
    }
    return int(d[op](n, m))
        # 많은 조건을 처리해야 할 때 (if-elif가 길어질 때),
        # lambda + dict 고려.
