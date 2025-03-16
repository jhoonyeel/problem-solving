def solution(emergency):
    sort = sorted(emergency, reverse=True)
    d = {el: rank + 1 for rank, el in enumerate(sort)}
    return [d[x] for x in emergency]