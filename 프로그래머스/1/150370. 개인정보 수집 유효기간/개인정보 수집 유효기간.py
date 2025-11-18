def solution(today, terms, privacies):
    today_y, today_m, today_d = map(int, today.split('.'))
    
    dic = {}
    for el in terms:
        x, long = el.split()
        dic[x] = int(long)
    
    res = []
    for idx, el in enumerate(privacies):
        date, t = el.split()
        y, m, d = map(int, date.split('.'))
        
        # 1) 개월 더하기
        m += dic[t]

        # 2) 12개월 단위로 연도 증가 처리
        y += (m - 1) // 12
        m = (m - 1) % 12 + 1

        # 3) 유효기간은 "만료일 - 1일"
        d -= 1
        if d == 0:         # 날짜가 0일이 되면 한 달 전으로 이동
            m -= 1
            d = 28
            if m == 0:
                y -= 1
                m = 12

        # 4) 오늘과 만료일 비교 (튜플 비교 사용)
        if (y, m, d) < (today_y, today_m, today_d):
            res.append(idx + 1)
    
    return res