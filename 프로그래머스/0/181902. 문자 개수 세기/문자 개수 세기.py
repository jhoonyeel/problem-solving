def solution(my_string):
    res = [0] * 52
    for x in my_string:
        asci = ord(x)
        if asci < 97:
            res[asci - 65] += 1
        else:
            res[asci - 71] += 1
    return res
    # print(ord('A'), ord('a'))
    # 65, 97