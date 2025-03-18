def solution(my_string):
    res = 0
    temp = ''
    for x in my_string:
        if x.isdigit(): # 숫자를 만나면
            temp += x # 임시 추가
        else: # 문자를 만나면
            if temp: # 기존의 temp값 추가
                res += int(temp)
                temp = ''
    # 마지막에 숫자로 끝나는 경우
    if temp:
        res += int(temp)
    return res