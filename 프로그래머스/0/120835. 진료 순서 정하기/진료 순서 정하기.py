def solution(emergency):
    res = []
    for i in emergency:
        idx = 1
        for j in emergency:
            if i < j:
                idx += 1
        res.append(idx)
    return res
