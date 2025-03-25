def solution(myStr):
    not_in_abc_lst = [x if x not in 'abc' else ' ' for x in myStr]
    word_lst = ''.join(not_in_abc_lst).split(' ')
    return [x for x in word_lst if x] or ['EMPTY']