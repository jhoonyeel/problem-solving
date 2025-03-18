def solution(n):
    pac = 1
    big_int = 2
    while n >= pac:
        pac *= big_int
        big_int += 1
    return big_int - 2