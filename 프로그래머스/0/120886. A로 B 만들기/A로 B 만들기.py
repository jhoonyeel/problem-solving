def solution(before, after):
    af = list(after)
    for x in before:
        try:
            idx = af.index(x)
            del af[idx]
        except:
            return 0
    return 1