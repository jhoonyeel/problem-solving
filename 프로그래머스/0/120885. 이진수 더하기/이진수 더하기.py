def solution(bin1, bin2):
    res1, res2 = 0, 0
    for i, b in enumerate(bin1[::-1]):
        res1 += int(b) * 2 ** i
    for i, b in enumerate(bin2[::-1]):
        res2 += int(b) * 2 ** i
    return bin(res1 + res2)[2:]