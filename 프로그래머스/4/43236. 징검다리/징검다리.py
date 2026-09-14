## 오답
# 바위 2개 다 제거해서, 해당 step 중 "사이 거리의 최솟값" 찾으면 되어 보임.
# 그렇지만 어떻게? -> 시뮬레이션? 다른 알고리즘? -> 직관이 보이진 않음.
# 따라서 전부 다 해보고 step들의 최솟값 비교하려고 함.
# 근데 복잡도 보면, dfs 바로 터지는 수준. 추가로 심지어 제거하는 바위 숫자도 변동.
# "제거할 바위 조합을 전부 만들어 보는 순간" -> 무조건 복잡도 터짐.

## 풀이
# 사고 전환 : 최소 거리를 x라고 미리 정해놓으면, 바위를 왼쪽부터 한 번만 순회하면서 x를 만족시키기 위해 몇 개를 제거해야 하는지 셀 수 있을까?
# -> 가능/불가능만 판정할 수 있음.
# 이분 탐색: 정답 후보를 가정 -> 참 / 거짓 판별 -> 단조성을 이용하여 나머지 후보 범위를 버림.

# 최소 거리 후보: 1, 2, 3, 4, ...
# 단조성을 지님. 바위를 n개 제거해서, 모든 구간의 거리를 "후보 거리" 이상으로 만들 수 있는가.

def solution(distance, rocks, n):
    srt = sorted(rocks)
    srt.append(distance)
    
    def check(candidate_minest):
        remove = 0
        prev_location = 0
        for r in srt:
            if r - prev_location < candidate_minest:
                remove += 1
            else:
                prev_location = r
        
        return remove <= n
    
    left = 1
    right = distance
    while left <= right:
        mid = (left + right) // 2
        
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return left - 1
