def solution(arr, queries):
    res = arr[:]
    for fir, sec in queries:
        res[fir], res[sec] = res[sec], res[fir]
    return res