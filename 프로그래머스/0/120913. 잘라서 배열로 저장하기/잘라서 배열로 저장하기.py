def solution(my_str, n):
    lst = []
    N = len(my_str) // n if len(my_str) % n == 0 else len(my_str) // n + 1
    for x in range(N):
        lst.append(my_str[n * x:n * (x + 1)])
    return lst