def solution(my_string):
    res = [0] * 52
    for x in my_string:
        asci = ord(x)
        if x.isupper():
            res[asci - 65] += 1
        else:
            res[asci - 71] += 1
    return res
    # print(ord('A'), ord('a'))
    # 65, 97