def solution(n, slicer, num_list):
    a, b, c = slicer
    
    start = 0 if n == 1 else a
    end = b + 1 if n in (1, 3, 4) else None
    step = c if n == 4 else None
    
    return num_list[start:end:step]