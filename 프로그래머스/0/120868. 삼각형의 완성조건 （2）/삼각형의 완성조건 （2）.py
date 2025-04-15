def solution(sides):
    big, small = max(sides), min(sides)
    return len(range(big - small + 1, big + small))
