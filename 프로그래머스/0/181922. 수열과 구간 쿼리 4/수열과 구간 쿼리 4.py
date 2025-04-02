def solution(arr, queries):
    res = arr[:]
    for s, e, k in queries:
        for i in range(s, e + 1):
            if i % k == 0:
                res[i] += 1
    return res