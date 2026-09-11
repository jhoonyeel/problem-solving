## 풀이
# 번호에 대한 개수를 매김.
# 적은 개수를 가진 번호부터 가져감. n/2까지 가져가기 반복.
# 전체 종류 리턴

def solution(nums):
    n = len(nums)
    d = {}
    for el in nums:
        d[el] = d.get(el, 0) + 1
    
    srt_d = sorted(d.items(), key=lambda x: x[1])
    
    res = {}
    for k, v in srt_d:
        if len(res) == n//2:
            break
        if v > 0:
            v -= 1
            res[k] = res.get(k, 0) + 1
    
    return len(res)
