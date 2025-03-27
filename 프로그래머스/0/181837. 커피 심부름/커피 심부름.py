def solution(order):
    total = 0
    for x in order:
        if 'cafelatte' in x:
            total += 5000
            continue
        total += 4500
    return total