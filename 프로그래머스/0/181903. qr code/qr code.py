def solution(q, r, code):
    return ''.join(v for i, v in enumerate(code) if i % q == r)
