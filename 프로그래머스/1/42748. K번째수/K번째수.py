## 풀이
# 예시 방법 그대로 1,2,3 순서대로 진행하면 되겠다 생각함. 딱히 다른 개선 구조가 없어보임.
# i, j, k 슬라이싱, sorted 활용해서 원본 배열 유지.
# 처음부터 저장할 공간 고려하여 빈 list 선언.

def solution(array, commands):
    res = []
    for i, j, k in commands:
        srt = sorted(array[i-1 : j])
        res.append(srt[k-1])
    
    return res