def solution(n):
    # [0] * 3 = [0, 0, 0]
    # 이게 range(3)으로 3번 반복됨.
    res = [[0] * n for _ in range(n)]

    for i in range(n):
        res[i][i] = 1
    return res