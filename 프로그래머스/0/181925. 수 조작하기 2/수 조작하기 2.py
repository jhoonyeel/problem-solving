def solution(numLog):
    d = {1:'w', -1:'s', 10:'d', -10:'a'}
    return ''.join(d[after - before] for before, after in zip(numLog, numLog[1:]))