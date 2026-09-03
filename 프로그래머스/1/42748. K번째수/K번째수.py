def solution(array, commands):
    res = []
    for i, j, k in commands:
        srt = sorted(array[i-1 : j])
        res.append(srt[k-1])
    
    return res