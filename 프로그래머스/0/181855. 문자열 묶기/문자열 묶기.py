def solution(strArr):
    order = [len(x) for x in strArr]
    size = {}
    for length in order:
        try:
            size[length] += 1
        except:
            size[length] = 1
    return max(size.values())