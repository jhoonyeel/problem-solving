from itertools import combinations

# “주문 → 조합 생성 → 카운트” 순서.
def solution(orders, course):
    res = []
    
    for cnt in course:
        freq = {}
        for order in orders:
            order = sorted(order)
            for c in combinations(order, cnt):
                freq[c] = freq.get(c, 0) + 1

        if not freq:
            continue

        max_cnt = max(freq.values())
        if max_cnt < 2:
            continue

        for k, v in freq.items():
            if v == max_cnt:
                res.append(''.join(k))

    return sorted(res)
