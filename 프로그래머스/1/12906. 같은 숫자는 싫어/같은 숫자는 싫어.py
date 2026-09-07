def solution(arr):
    stk = []
    prev = ''
    for el in arr:
        if el == prev:
            continue
        else:
            stk.append(el)
        prev = el
    
    return stk