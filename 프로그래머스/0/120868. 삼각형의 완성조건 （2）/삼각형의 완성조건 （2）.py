def solution(sides):
    big, small = max(sides), min(sides)
    return len(range(big - small + 1, big + small))
    # 삼각형 조건: 가장 긴 변 < 나머지 두 변의 합
    # 세 변이 a, b, c일 때
    # ⇒ max(a, b, c) < sum(other two)
    
    # |a - b| + 1 ≤ c < a + b
    # (a + b - 1) - (|a - b|) = 2 * min - 1