def solution(my_string, overwrite_string, s):
    lst1 = list(my_string)
    lst2 = list(overwrite_string)
    lst1[s:s + len(lst2)] = lst2
    return ''.join(lst1)
    # 리스트의 슬라이스 구간에 b 리스트의 "요소"를 할당
    # 문자열은 immutable(불변) → 부분 수정 불가