## 풀이
# 기존 풀이가 언 뜻 보이고, 완전탐색 섹션의 문제라, dfs 활용하는 것인지 넘어갈 뻔 했음.
# 다만, 문제를 봤을 때 하나의 명함의 값을 (w <= h) 구조로 유지하도록 swap하는 방식이 떠오름.
# 충분히 swap과 max값을 순회하며 다룬다면, 계산 가능할 것으로 판단하여 풀이함.

def solution(sizes):
    max_w, max_h = float('-inf'), float('-inf')
    for w, h in sizes:
        if w > h:
            w, h = h, w
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    
    return max_w * max_h