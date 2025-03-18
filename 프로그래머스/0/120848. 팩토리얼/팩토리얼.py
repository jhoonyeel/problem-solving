def solution(n):
    # 초기 상태 1!으로 설정
    pac = 1
    biggest = 1
    # 이후 반복문에서 2!부터 시작
    while pac <= n:
        biggest += 1
        pac *= biggest
    return biggest - 1