def solution(arr):
    l_idx, r_idx = -1, -1
    for i, v in enumerate(arr):
        if l_idx == -1 and v == 2:
            l_idx, r_idx = i, i
        if l_idx != -1 and v == 2:
            r_idx = i
    
    if l_idx == -1:
        return [-1]
    else:
        return arr[l_idx:r_idx + 1]
        