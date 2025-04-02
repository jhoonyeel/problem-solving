def solution(arr):
    i = 0
    stk = []
    N = len(arr)
    while i < N:
        if not stk:
            stk.append(arr[i])
            i += 1
            continue
        if stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1
    return stk or [-1]