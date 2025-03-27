def solution(arr):
    if 2 not in arr:
        return [-1]
    l_idx, r_idx = arr.index(2), len(arr) - arr[::-1].index(2)
    return arr[l_idx:r_idx]