def solution(strArr):
    order = [len(x) for x in strArr]
    size = {}
    for length in order:
        if length in size:
            size[length] += 1
        else:
            size[length] = 1
    return max(size.values())