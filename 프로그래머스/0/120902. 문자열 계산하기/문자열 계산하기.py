def solution(my_string):
    lst = my_string.split()
    total = int(lst[0])
    for idx in range(1, len(lst), 2):
        op = lst[idx]
        if op == '+':
            total += int(lst[idx + 1])
        elif op == '-':
            total -= int(lst[idx + 1])
    return total