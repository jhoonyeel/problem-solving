def solution(my_strings, parts):
    res = []
    for string, (start, end) in zip(my_strings, parts):
        res.append(string[start : end + 1])
    return ''.join(res)
    # res 문자열을 계속 변경시키면 N^2 복잡도
    # 따라서 리스트에 문자열로 보관 후, 한번에 join처리하여 N 복잡도