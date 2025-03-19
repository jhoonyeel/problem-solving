def solution(strArr):
    size = {}
    for x in strArr:
        size[len(x)] = size.get(len(x), 0) + 1
    return max(size.values())
    # order = [len(x) for x in strArr]
    # 리스트를 통해 len(x) 중복을 줄이면, 오히려 공간 복잡도가 더 커짐.