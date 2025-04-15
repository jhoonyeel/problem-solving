def solution(sides):
    big, small = max(sides), min(sides)
    res = 0
    for x in range(big - small + 1, big + small):
        res += 1
    return res