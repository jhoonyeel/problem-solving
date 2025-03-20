def solution(n):
    cnt = 0
    for x in range(4, n + 1):
        for div in range(2, int(x ** 0.5) + 1):
            if x % div == 0:
                cnt += 1
                break
    return cnt
    # Ⅰ. 전체 - 소수의 개수
    # Ⅱ. 약수 3개 이상 카운트
